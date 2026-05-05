# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T16:14:13.999763+00:00`
- Correlation status: `ready`
- Asset price records: `372`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0887` n `7`; crypto_alt avg `0.0638` n `223`; crypto_major avg `-0.0828` n `7`; equity avg `-0.1964` n `47`; fx avg `-0.0016` n `4`; index avg `0.0587` n `6`; metal avg `-0.1894` n `7`; unknown avg `1.1639` n `313`
- 1h: commodity avg `-0.2533` n `7`; crypto_alt avg `-0.162` n `223`; crypto_major avg `0.1353` n `7`; equity avg `0.0149` n `47`; fx avg `-0.1445` n `4`; index avg `0.2798` n `6`; metal avg `-0.3411` n `7`; unknown avg `1.1404` n `313`
- 4h: commodity avg `-0.6665` n `7`; crypto_alt avg `-0.0808` n `223`; crypto_major avg `0.3812` n `7`; equity avg `0.4545` n `47`; fx avg `-0.1124` n `4`; index avg `0.8039` n `6`; metal avg `-0.3441` n `7`; unknown avg `1.4292` n `312`
- 24h: commodity avg `-1.2348` n `7`; crypto_alt avg `1.8779` n `223`; crypto_major avg `2.3314` n `7`; equity avg `1.2329` n `47`; fx avg `-0.0568` n `4`; index avg `1.1045` n `6`; metal avg `0.9354` n `7`; unknown avg `2.1484` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `368`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2009`, n `368`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `368`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `368`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `368`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1058`, n `364`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `368`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `368`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.103`, n `368`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0976`, n `364`, weak_sample_signal
