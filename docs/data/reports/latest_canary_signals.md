# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T12:11:38.500841+00:00`
- Correlation status: `ready`
- Asset price records: `358`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1318` n `7`; crypto_alt avg `0.0623` n `223`; crypto_major avg `0.1128` n `7`; equity avg `0.1853` n `47`; fx avg `0.0063` n `4`; index avg `0.1577` n `6`; metal avg `0.1816` n `7`; unknown avg `-0.0589` n `312`
- 1h: commodity avg `-0.3321` n `7`; crypto_alt avg `0.1216` n `223`; crypto_major avg `0.2505` n `7`; equity avg `0.3218` n `47`; fx avg `0.0129` n `4`; index avg `0.117` n `6`; metal avg `0.5971` n `7`; unknown avg `-0.1484` n `312`
- 4h: commodity avg `-0.3022` n `7`; crypto_alt avg `0.3002` n `223`; crypto_major avg `0.4265` n `7`; equity avg `0.5599` n `47`; fx avg `0.075` n `4`; index avg `0.2239` n `6`; metal avg `0.5306` n `7`; unknown avg `-0.0896` n `312`
- 24h: commodity avg `0.1613` n `7`; crypto_alt avg `2.3982` n `223`; crypto_major avg `2.3049` n `7`; equity avg `0.7627` n `47`; fx avg `0.0739` n `4`; index avg `0.4547` n `6`; metal avg `1.0039` n `7`; unknown avg `-0.2141` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `354`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2057`, n `354`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `354`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.132`, n `354`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `354`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `354`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `354`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `354`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.103`, n `350`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0889`, n `350`, weak_sample_signal
