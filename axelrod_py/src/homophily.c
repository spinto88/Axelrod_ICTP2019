#include "homophily.h"

double homophily(axl_agent a, axl_agent b)
{
	int i;
	int f = a.f; /* Number of features.*/
	double hab = 0.00; /* Homophily.*/
 
	/* Go over all features. */
	for(i = 0; i < f; i++)
	{
 		/* If a given feature is shared, the homophily increases. */
		if(a.feat[i] == b.feat[i])
			hab += 1.00;
	}

	/* Return the normalized (respect to f) homophily. */
	return (hab / f);
}

double homophily_with_mm(axl_agent a, axl_mass_media b)
{
	int i;
	int f = a.f; /* Number of features.*/
	double hab = 0.00; /* Homophily.*/
 
	/* Go over all features. */
	for(i = 0; i < f; i++)
	{
 		/* If a given feature is shared, the homophily increases. */
		if(a.feat[i] == b.feat[i])
			hab += 1.00;
	}

	/* Return the normalized (respect to f) homophily. */
	return (hab / f);
}
