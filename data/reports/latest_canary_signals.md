# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T13:30:35.896392+00:00`
- Correlation status: `ready`
- Asset price records: `364`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `7`; crypto_alt avg `-0.221` n `223`; crypto_major avg `-0.1883` n `7`; equity avg `-0.321` n `47`; fx avg `-0.0055` n `4`; index avg `-0.0034` n `6`; metal avg `-0.0643` n `7`; unknown avg `0.0285` n `312`
- 1h: commodity avg `0.0134` n `7`; crypto_alt avg `0.0958` n `223`; crypto_major avg `0.2315` n `7`; equity avg `-0.3495` n `47`; fx avg `0.0073` n `4`; index avg `0.1845` n `6`; metal avg `-0.164` n `7`; unknown avg `-0.009` n `312`
- 4h: commodity avg `-0.2877` n `7`; crypto_alt avg `0.4737` n `223`; crypto_major avg `1.0223` n `7`; equity avg `-0.0697` n `47`; fx avg `0.0503` n `4`; index avg `0.416` n `6`; metal avg `0.3347` n `7`; unknown avg `0.2592` n `312`
- 24h: commodity avg `0.1487` n `7`; crypto_alt avg `2.4531` n `223`; crypto_major avg `2.565` n `7`; equity avg `0.4041` n `47`; fx avg `0.0809` n `4`; index avg `0.6523` n `6`; metal avg `0.7709` n `7`; unknown avg `0.1436` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2087`, n `360`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2016`, n `360`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.134`, n `360`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.13`, n `360`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.108`, n `360`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `360`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `360`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `360`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0914`, n `356`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `360`, weak_sample_signal
