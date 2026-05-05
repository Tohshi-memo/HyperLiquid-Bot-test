# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T07:30:32.951296+00:00`
- Correlation status: `ready`
- Asset price records: `340`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `7`; crypto_alt avg `0.2999` n `223`; crypto_major avg `0.0351` n `7`; equity avg `0.0024` n `47`; fx avg `-0.0059` n `4`; index avg `-0.2118` n `6`; metal avg `-0.0551` n `7`; unknown avg `0.0376` n `312`
- 1h: commodity avg `-0.1936` n `7`; crypto_alt avg `0.4235` n `223`; crypto_major avg `0.283` n `7`; equity avg `0.3305` n `47`; fx avg `-0.0087` n `4`; index avg `-0.0054` n `6`; metal avg `0.2469` n `7`; unknown avg `0.1499` n `312`
- 4h: commodity avg `-0.0183` n `7`; crypto_alt avg `0.3356` n `223`; crypto_major avg `0.538` n `7`; equity avg `1.0256` n `47`; fx avg `-0.0074` n `4`; index avg `0.191` n `6`; metal avg `0.4314` n `7`; unknown avg `1.5053` n `310`
- 24h: commodity avg `0.7213` n `7`; crypto_alt avg `1.1491` n `223`; crypto_major avg `0.5916` n `7`; equity avg `0.0164` n `47`; fx avg `-0.0319` n `4`; index avg `-0.2974` n `6`; metal avg `-0.7427` n `7`; unknown avg `1.2766` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2201`, n `336`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2132`, n `336`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `336`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1344`, n `336`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1237`, n `336`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `336`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1075`, n `336`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1067`, n `336`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `332`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0961`, n `332`, weak_sample_signal
