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
#include <math.h>
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
        return 7;
    }

    void derivatives
    (
        const scalar x,
        const scalarField& y,
        scalarField& dydx
    ) const
    {
// Info << "SEX1" << endl;
// for (int i = 0; i < 7; i++)
// {
//     Info << y[i] << " ";
// } Info << endl;
dydx[0] =  - 1 * 910000000.0 * Foam::pow(y[0], 0.54) * Foam::pow(y[2], 0.5) * Foam::exp(-7.7168260359000165) + 1 * 22600000000000.0 * Foam::pow(y[3], 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275) + 2 * 1840000.0 * Foam::pow(y[4], 0.2) * Foam::pow(y[2], 0.5) * Foam::exp(-10.904210702902198) + 2 * 300000000000000.0 * Foam::pow(y[4], 1) * Foam::pow(y[0], 1) * Foam::exp(-6.710283509478275) - 1 * 300000000000000.0 * Foam::pow(y[4], 1) * Foam::pow(y[0], 1) * Foam::exp(-6.710283509478275) + 2 * 200000000000.0 * Foam::pow(y[6], 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dydx[1] =  + 1 * 910000000.0 * Foam::pow(y[0], 0.54) * Foam::pow(y[2], 0.5) * Foam::exp(-7.7168260359000165) - 1 * 22600000000000.0 * Foam::pow(y[3], 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275) - 1 * 200000000000.0 * Foam::pow(y[6], 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dydx[2] =  - 0.5 * 910000000.0 * Foam::pow(y[0], 0.54) * Foam::pow(y[2], 0.5) * Foam::exp(-7.7168260359000165) - 0.5 * 142000000.0 * Foam::pow(y[3], 0.95) * Foam::pow(y[2], 0.5) * Foam::exp(-14.292903875188726) - 0.5 * 1840000.0 * Foam::pow(y[4], 0.2) * Foam::pow(y[2], 0.5) * Foam::exp(-10.904210702902198);
dydx[3] =  - 1 * 142000000.0 * Foam::pow(y[3], 0.95) * Foam::pow(y[2], 0.5) * Foam::exp(-14.292903875188726) - 1 * 22600000000000.0 * Foam::pow(y[3], 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275) + 1 * 1840000.0 * Foam::pow(y[4], 0.2) * Foam::pow(y[2], 0.5) * Foam::exp(-10.904210702902198) + 1 * 200000000000.0 * Foam::pow(y[6], 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dydx[4] =  - 1 * 1840000.0 * Foam::pow(y[4], 0.2) * Foam::pow(y[2], 0.5) * Foam::exp(-10.904210702902198) - 1 * 300000000000000.0 * Foam::pow(y[4], 1) * Foam::pow(y[0], 1) * Foam::exp(-6.710283509478275);
dydx[5] =  + 1 * 142000000.0 * Foam::pow(y[3], 0.95) * Foam::pow(y[2], 0.5) * Foam::exp(-14.292903875188726) + 1 * 22600000000000.0 * Foam::pow(y[3], 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dydx[6] =  + 1 * 300000000000000.0 * Foam::pow(y[4], 1) * Foam::pow(y[0], 1) * Foam::exp(-6.710283509478275) - 1 * 200000000000.0 * Foam::pow(y[6], 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
// Info << "SEX2" << endl;

    }

    void jacobian
    (
        const scalar x,
        const scalarField& y,
        scalarField& dfdx,
        scalarSquareMatrix& dfdy
    ) const
    {
        dfdx[0] = dfdx[1] = dfdx[2] = dfdx[3] = dfdx[4] = dfdx[5] = dfdx[6] = 0.0;
// Info << "SEX2" << endl;

dfdy(0, 0) = 0 - 1 * 910000000.0 * 0.54 * Foam::pow(y[0], 0.54 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-7.7168260359000165) + 2 * 300000000000000.0 * 1 * Foam::pow(y[4], 1) * Foam::pow(y[0], 1 - 1) * Foam::exp(-6.710283509478275) - 1 * 300000000000000.0 * 1 * Foam::pow(y[4], 1) * Foam::pow(y[0], 1 - 1) * Foam::exp(-6.710283509478275);
dfdy(0, 1) = 0 + 1 * 22600000000000.0 * 1 * Foam::pow(y[3], 1) * Foam::pow(y[1], 1 - 1) * Foam::exp(-6.710283509478275) + 2 * 200000000000.0 * 1 * Foam::pow(y[6], 1) * Foam::pow(y[1], 1 - 1) * Foam::exp(-6.710283509478275);
dfdy(0, 2) = 0 - 1 * 910000000.0 * 0.5 * Foam::pow(y[0], 0.54) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-7.7168260359000165) + 2 * 1840000.0 * 0.5 * Foam::pow(y[4], 0.2) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-10.904210702902198);
dfdy(0, 3) = 0 + 1 * 22600000000000.0 * 1 * Foam::pow(y[3], 1 - 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dfdy(0, 4) = 0 + 2 * 1840000.0 * 0.2 * Foam::pow(y[4], 0.2 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-10.904210702902198) + 2 * 300000000000000.0 * 1 * Foam::pow(y[4], 1 - 1) * Foam::pow(y[0], 1) * Foam::exp(-6.710283509478275) - 1 * 300000000000000.0 * 1 * Foam::pow(y[4], 1 - 1) * Foam::pow(y[0], 1) * Foam::exp(-6.710283509478275);
dfdy(0, 5) = 0;
dfdy(0, 6) = 0 + 2 * 200000000000.0 * 1 * Foam::pow(y[6], 1 - 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dfdy(1, 0) = 0 + 1 * 910000000.0 * 0.54 * Foam::pow(y[0], 0.54 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-7.7168260359000165);
dfdy(1, 1) = 0 - 1 * 22600000000000.0 * 1 * Foam::pow(y[3], 1) * Foam::pow(y[1], 1 - 1) * Foam::exp(-6.710283509478275) - 1 * 200000000000.0 * 1 * Foam::pow(y[6], 1) * Foam::pow(y[1], 1 - 1) * Foam::exp(-6.710283509478275);
dfdy(1, 2) = 0 + 1 * 910000000.0 * 0.5 * Foam::pow(y[0], 0.54) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-7.7168260359000165);
dfdy(1, 3) = 0 - 1 * 22600000000000.0 * 1 * Foam::pow(y[3], 1 - 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dfdy(1, 4) = 0;
dfdy(1, 5) = 0;
dfdy(1, 6) = 0 - 1 * 200000000000.0 * 1 * Foam::pow(y[6], 1 - 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dfdy(2, 0) = 0 - 0.5 * 910000000.0 * 0.54 * Foam::pow(y[0], 0.54 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-7.7168260359000165);
dfdy(2, 1) = 0;
dfdy(2, 2) = 0 - 0.5 * 910000000.0 * 0.5 * Foam::pow(y[0], 0.54) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-7.7168260359000165) - 0.5 * 142000000.0 * 0.5 * Foam::pow(y[3], 0.95) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-14.292903875188726) - 0.5 * 1840000.0 * 0.5 * Foam::pow(y[4], 0.2) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-10.904210702902198);
dfdy(2, 3) = 0 - 0.5 * 142000000.0 * 0.95 * Foam::pow(y[3], 0.95 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-14.292903875188726);
dfdy(2, 4) = 0 - 0.5 * 1840000.0 * 0.2 * Foam::pow(y[4], 0.2 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-10.904210702902198);
dfdy(2, 5) = 0;
dfdy(2, 6) = 0;
dfdy(3, 0) = 0;
dfdy(3, 1) = 0 - 1 * 22600000000000.0 * 1 * Foam::pow(y[3], 1) * Foam::pow(y[1], 1 - 1) * Foam::exp(-6.710283509478275) + 1 * 200000000000.0 * 1 * Foam::pow(y[6], 1) * Foam::pow(y[1], 1 - 1) * Foam::exp(-6.710283509478275);
dfdy(3, 2) = 0 - 1 * 142000000.0 * 0.5 * Foam::pow(y[3], 0.95) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-14.292903875188726) + 1 * 1840000.0 * 0.5 * Foam::pow(y[4], 0.2) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-10.904210702902198);
dfdy(3, 3) = 0 - 1 * 142000000.0 * 0.95 * Foam::pow(y[3], 0.95 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-14.292903875188726) - 1 * 22600000000000.0 * 1 * Foam::pow(y[3], 1 - 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dfdy(3, 4) = 0 + 1 * 1840000.0 * 0.2 * Foam::pow(y[4], 0.2 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-10.904210702902198);
dfdy(3, 5) = 0;
dfdy(3, 6) = 0 + 1 * 200000000000.0 * 1 * Foam::pow(y[6], 1 - 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dfdy(4, 0) = 0 - 1 * 300000000000000.0 * 1 * Foam::pow(y[4], 1) * Foam::pow(y[0], 1 - 1) * Foam::exp(-6.710283509478275);
dfdy(4, 1) = 0;
dfdy(4, 2) = 0 - 1 * 1840000.0 * 0.5 * Foam::pow(y[4], 0.2) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-10.904210702902198);
dfdy(4, 3) = 0;
dfdy(4, 4) = 0 - 1 * 1840000.0 * 0.2 * Foam::pow(y[4], 0.2 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-10.904210702902198) - 1 * 300000000000000.0 * 1 * Foam::pow(y[4], 1 - 1) * Foam::pow(y[0], 1) * Foam::exp(-6.710283509478275);
dfdy(4, 5) = 0;
dfdy(4, 6) = 0;
dfdy(5, 0) = 0;
dfdy(5, 1) = 0 + 1 * 22600000000000.0 * 1 * Foam::pow(y[3], 1) * Foam::pow(y[1], 1 - 1) * Foam::exp(-6.710283509478275);
dfdy(5, 2) = 0 + 1 * 142000000.0 * 0.5 * Foam::pow(y[3], 0.95) * Foam::pow(y[2], 0.5 - 1) * Foam::exp(-14.292903875188726);
dfdy(5, 3) = 0 + 1 * 142000000.0 * 0.95 * Foam::pow(y[3], 0.95 - 1) * Foam::pow(y[2], 0.5) * Foam::exp(-14.292903875188726) + 1 * 22600000000000.0 * 1 * Foam::pow(y[3], 1 - 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);
dfdy(5, 4) = 0;
dfdy(5, 5) = 0;
dfdy(5, 6) = 0;
dfdy(6, 0) = 0 + 1 * 300000000000000.0 * 1 * Foam::pow(y[4], 1) * Foam::pow(y[0], 1 - 1) * Foam::exp(-6.710283509478275);
dfdy(6, 1) = 0 - 1 * 200000000000.0 * 1 * Foam::pow(y[6], 1) * Foam::pow(y[1], 1 - 1) * Foam::exp(-6.710283509478275);
dfdy(6, 2) = 0;
dfdy(6, 3) = 0;
dfdy(6, 4) = 0 + 1 * 300000000000000.0 * 1 * Foam::pow(y[4], 1 - 1) * Foam::pow(y[0], 1) * Foam::exp(-6.710283509478275);
dfdy(6, 5) = 0;
dfdy(6, 6) = 0 - 1 * 200000000000.0 * 1 * Foam::pow(y[6], 1 - 1) * Foam::pow(y[1], 1) * Foam::exp(-6.710283509478275);

// Info << "SEX" << endl;

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
    scalar xEnd = 1e-10;
    scalarField yStart(ode.nEqns());

    yStart[0] = 0.0197; // H2
    yStart[4] = 0.0673; // CH4
    yStart[2] = 0.2126; // O2

    yStart[1] = yStart[3] = yStart[5] = yStart[6] = 1e-12;

    // Print the evolution of the solution and the time-step
    scalarField dyStart(ode.nEqns());
    scalarField dfdx(ode.nEqns());
    scalarSquareMatrix dfdy(ode.nEqns());
    ode.derivatives(xStart, yStart, dyStart);
    // ode.jacobian(xStart, yStart, dfdx, dfdy);

    Info<< setw(10) << "relTol" << setw(12) <<  "Time" <<  endl;
    Info<< setw(10) << std::pow(5.0, -0.2) <<  endl;
    Info<< setw(10) << "SEX" <<  endl;
    Info<< setprecision(6);

    scalar dxEst = 1e-15;
    auto prev =std:: chrono::high_resolution_clock::now();


    for (label i=7; i<20; i++)
    {
        scalar relTol = ::Foam::exp(-scalar(i + 1));

        scalarField y(yStart);
        odeSolver->relTol() = relTol;
        odeSolver->absTol() = relTol;
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
