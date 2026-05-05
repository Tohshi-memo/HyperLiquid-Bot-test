# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T06:30:31.173761+00:00`
- Correlation status: `ready`
- Asset price records: `336`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0708` n `7`; crypto_alt avg `-0.1635` n `223`; crypto_major avg `-0.1346` n `7`; equity avg `0.0245` n `47`; fx avg `-0.0018` n `4`; index avg `-0.0336` n `6`; metal avg `-0.0608` n `7`; unknown avg `-0.0224` n `312`
- 1h: commodity avg `0.2098` n `7`; crypto_alt avg `-0.1222` n `223`; crypto_major avg `-0.1457` n `7`; equity avg `-0.0317` n `47`; fx avg `0.0163` n `4`; index avg `0.0167` n `6`; metal avg `-0.0557` n `7`; unknown avg `-0.0438` n `310`
- 4h: commodity avg `0.2189` n `7`; crypto_alt avg `-0.124` n `223`; crypto_major avg `0.3952` n `7`; equity avg `0.6016` n `47`; fx avg `-0.0022` n `4`; index avg `0.2321` n `6`; metal avg `-0.0604` n `7`; unknown avg `1.3219` n `310`
- 24h: commodity avg `1.3635` n `7`; crypto_alt avg `0.9443` n `223`; crypto_major avg `0.483` n `7`; equity avg `-0.2344` n `47`; fx avg `-0.0286` n `4`; index avg `-0.2073` n `6`; metal avg `-1.4302` n `7`; unknown avg `0.6417` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2223`, n `332`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2156`, n `332`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1396`, n `332`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `332`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1336`, n `332`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `332`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `332`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `332`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1044`, n `328`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1042`, n `328`, weak_sample_signal
