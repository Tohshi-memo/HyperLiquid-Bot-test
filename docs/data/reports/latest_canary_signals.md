# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T13:19:17.993776+00:00`
- Correlation status: `ready`
- Asset price records: `457`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0483` n `7`; crypto_alt avg `-0.0674` n `223`; crypto_major avg `0.0126` n `7`; equity avg `0.0644` n `47`; fx avg `-0.0125` n `4`; index avg `0.0195` n `6`; metal avg `0.0003` n `7`; unknown avg `-0.0339` n `313`
- 1h: commodity avg `0.3662` n `7`; crypto_alt avg `-0.5571` n `223`; crypto_major avg `-0.8005` n `7`; equity avg `-0.4113` n `47`; fx avg `0.0368` n `4`; index avg `-0.2015` n `6`; metal avg `-0.0266` n `7`; unknown avg `1.2351` n `313`
- 4h: commodity avg `0.0302` n `7`; crypto_alt avg `-0.2878` n `223`; crypto_major avg `0.1152` n `7`; equity avg `-0.3928` n `47`; fx avg `0.0385` n `4`; index avg `-0.0594` n `6`; metal avg `-0.0414` n `7`; unknown avg `0.1771` n `313`
- 24h: commodity avg `-2.4983` n `7`; crypto_alt avg `2.6129` n `223`; crypto_major avg `1.5591` n `7`; equity avg `2.4592` n `47`; fx avg `-0.5682` n `4`; index avg `2.3112` n `6`; metal avg `2.1007` n `7`; unknown avg `2.9659` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1647`, n `453`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1588`, n `453`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1413`, n `453`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1254`, n `453`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `453`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `453`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0951`, n `449`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `453`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `453`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `449`, weak_sample_signal
