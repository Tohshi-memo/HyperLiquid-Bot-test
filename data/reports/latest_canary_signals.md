# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T17:30:28.072717+00:00`
- Correlation status: `ready`
- Asset price records: `378`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1325` n `7`; crypto_alt avg `0.0576` n `223`; crypto_major avg `0.2998` n `7`; equity avg `0.0374` n `47`; fx avg `0.0016` n `4`; index avg `0.1432` n `6`; metal avg `0.0668` n `7`; unknown avg `0.0187` n `313`
- 1h: commodity avg `-0.145` n `7`; crypto_alt avg `0.0133` n `223`; crypto_major avg `0.1728` n `7`; equity avg `0.1822` n `47`; fx avg `0.0084` n `4`; index avg `0.1848` n `6`; metal avg `0.0307` n `7`; unknown avg `-0.0452` n `313`
- 4h: commodity avg `-0.5718` n `7`; crypto_alt avg `-0.3095` n `223`; crypto_major avg `0.0162` n `7`; equity avg `0.7774` n `47`; fx avg `-0.134` n `4`; index avg `0.7228` n `6`; metal avg `-0.4704` n `7`; unknown avg `0.0871` n `312`
- 24h: commodity avg `-1.3085` n `7`; crypto_alt avg `1.2103` n `223`; crypto_major avg `1.6376` n `7`; equity avg `1.4856` n `47`; fx avg `-0.044` n `4`; index avg `1.3548` n `6`; metal avg `0.758` n `7`; unknown avg `0.7474` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.207`, n `374`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2002`, n `374`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `374`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `374`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1098`, n `370`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1086`, n `374`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `374`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `374`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `374`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1017`, n `370`, weak_sample_signal
