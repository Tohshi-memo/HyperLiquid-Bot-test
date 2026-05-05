# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T19:30:27.385078+00:00`
- Correlation status: `ready`
- Asset price records: `386`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `7`; crypto_alt avg `0.2457` n `223`; crypto_major avg `0.2075` n `7`; equity avg `-0.0852` n `47`; fx avg `0.0066` n `4`; index avg `-0.0025` n `6`; metal avg `-0.0068` n `7`; unknown avg `0.0689` n `313`
- 1h: commodity avg `0.0185` n `7`; crypto_alt avg `0.3145` n `223`; crypto_major avg `0.1717` n `7`; equity avg `-0.1027` n `47`; fx avg `0.0159` n `4`; index avg `0.1217` n `6`; metal avg `-0.1702` n `7`; unknown avg `1.1561` n `313`
- 4h: commodity avg `0.0677` n `7`; crypto_alt avg `0.4833` n `223`; crypto_major avg `0.1746` n `7`; equity avg `-0.1394` n `47`; fx avg `0.0228` n `4`; index avg `0.2037` n `6`; metal avg `-0.5997` n `7`; unknown avg `1.1753` n `313`
- 24h: commodity avg `-1.1977` n `7`; crypto_alt avg `1.7482` n `223`; crypto_major avg `2.3838` n `7`; equity avg `1.5786` n `47`; fx avg `-0.0261` n `4`; index avg `1.4907` n `6`; metal avg `0.6431` n `7`; unknown avg `2.0193` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `382`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2001`, n `382`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1316`, n `382`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1275`, n `382`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1137`, n `378`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `382`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1061`, n `382`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1058`, n `378`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `382`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `382`, weak_sample_signal
