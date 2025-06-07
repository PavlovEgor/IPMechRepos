/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2011-2016 OpenFOAM Foundation
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Description

\*---------------------------------------------------------------------------*/

#include "argList.H"
#include "IOmanip.H"
#include "ODESystem.H"
#include "ODESolver.H"
#include <ctime>
#include <chrono>
#include <algorithm>
using namespace Foam;

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

class testODE
:
    public ODESystem
{

public:

    testODE()
    {}

    label nEqns() const
    {
        return 8;
    }

    void derivatives
    (
        const scalar x,
        const scalarField& y,
        scalarField& dydx
    ) const
    {
        dydx[0] = -1.71 * y[0] + 0.43 * y[1] + 8.32 * y[2] + 0.0007;
        dydx[1] = 1.71 * y[0] - 8.75 * y[1];
        dydx[2] = -10.03 * y[2] + 0.43 * y[3] + 0.035 * y[4];
        dydx[3] = 8.32 * y[1] + 1.71 * y[2] - 1.12 * y[3];
        dydx[4] = -1.745 * y[4] + 0.43 * y[5] + 0.43 * y[6];
        dydx[5] = -280 * y[5] * y[7] + 0.69 * y[3] + 1.71 * y[4] - 0.43 * y[5] + 0.69 * y[6];
        dydx[6] = 280 * y[5] * y[7] - 1.81 * y[6];
        dydx[7] = - dydx[6];
    }

    void jacobian
    (
        const scalar x,
        const scalarField& y,
        scalarField& dfdx,
        scalarSquareMatrix& dfdy
    ) const
    {
        dfdx[0] = dfdx[1] = dfdx[2] = dfdx[3] = dfdx[4] = dfdx[5] = dfdx[6] = dfdx[7] = 0.0;

        dfdy(0, 0) = -1.71;
        dfdy(0, 1) = 0.43;
        dfdy(0, 2) = 8.32;
        dfdy(0, 3) = 0.0;
        dfdy(0, 4) = 0.0;
        dfdy(0, 5) = 0.0;
        dfdy(0, 6) = 0.0;
        dfdy(0, 7) = 0.0;

        dfdy(1, 0) = 1.71;
        dfdy(1, 1) = -8.75;
        dfdy(1, 2) = 0.0;
        dfdy(1, 3) = 0.0;
        dfdy(1, 4) = 0.0;
        dfdy(1, 5) = 0.0;
        dfdy(1, 6) = 0.0;
        dfdy(1, 7) = 0.0;

        dfdy(2, 0) = 0.0;
        dfdy(2, 1) = 0.0;
        dfdy(2, 2) = -10.03;
        dfdy(2, 3) = 0.43;
        dfdy(2, 4) = 0.035;
        dfdy(2, 5) = 0.0;
        dfdy(2, 6) = 0.0;
        dfdy(2, 7) = 0.0;

        dfdy(3, 0) = 0.0;
        dfdy(3, 1) = 8.32;
        dfdy(3, 2) = 1.71;
        dfdy(3, 3) = -1.12;
        dfdy(3, 4) = 0.0;
        dfdy(3, 5) = 0.0;
        dfdy(3, 6) = 0.0;
        dfdy(3, 7) = 0.0;

        dfdy(4, 0) = 0.0;
        dfdy(4, 1) = 0.0;
        dfdy(4, 2) = 0.0;
        dfdy(4, 3) = 0.0;
        dfdy(4, 4) = -1.745;
        dfdy(4, 5) = 0.43;
        dfdy(4, 6) = 0.43;
        dfdy(4, 7) = 0.0;

        dfdy(5, 0) = 0.0;
        dfdy(5, 1) = 0.0;
        dfdy(5, 2) = 0.0;
        dfdy(5, 3) = 0.69;
        dfdy(5, 4) = 1.71;
        dfdy(5, 5) = -280 * y[7] - 0.43;
        dfdy(5, 6) = 0.69;
        dfdy(5, 7) = -280 * y[5];

        dfdy(6, 1) = 0.0;
        dfdy(6, 0) = 0.0;
        dfdy(6, 2) = 0.0;
        dfdy(6, 3) = 0.0;
        dfdy(6, 4) = 0.0;
        dfdy(6, 5) = 280 * y[7];
        dfdy(6, 6) = -1.81;
        dfdy(6, 7) = 280 * y[5];

        dfdy(7, 1) = -8.75;
        dfdy(7, 0) = 1.71;
        dfdy(7, 2) = 0.0;
        dfdy(7, 3) = 0.0;
        dfdy(7, 4) = 0.0;
        dfdy(7, 5) = -280 * y[7];
        dfdy(7, 6) = -1.81;
        dfdy(7, 7) = -280 * y[5];
    }
};


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Main program:

int main(int argc, char *argv[])
{
    argList::addArgument("ODESolver");
    argList args(argc, argv);
    // Create the ODE system
    testODE ode;

    dictionary dict;
    dict.add("solver", args[1]);

    // Create the selected ODE system solver
    autoPtr<ODESolver> odeSolver = ODESolver::New(ode, dict);

    // Initialise the ODE system fields
    scalar xStart = 0;
    scalar xEnd = 321.8122;
    scalarField yStart(ode.nEqns());
    yStart[0] = 1.0;
    yStart[1] = yStart[2] = yStart[3] = yStart[4] = yStart[5] = yStart[6] = 0.0;
    yStart[7] = 0.0057;

    // Print the evolution of the solution and the time-step
    scalarField dyStart(ode.nEqns());
    ode.derivatives(xStart, yStart, dyStart);

    Info<< setw(10) << "relTol" << setw(12) <<  "Time" <<  endl;
    Info<< setprecision(6);

    scalar dxEst = 0.001;
    auto prev =std:: chrono::high_resolution_clock::now();


    for (label i=0; i<20; i++)
    {
        scalar relTol = ::Foam::exp(-scalar(i + 1));

        scalarField y(yStart);

        odeSolver->relTol() = relTol;
        odeSolver->solve(xStart, xEnd, y, dxEst);
	
	std::chrono::high_resolution_clock::time_point cur = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> time_span = cur - prev;
	
        Info<< scientific << setw(13) << relTol;
        Info<< fixed << setw(11) << time_span.count()
            << endl;
	prev = cur;
    }



    return 0;
}


// ************************************************************************* //
