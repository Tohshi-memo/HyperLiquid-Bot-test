# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T19:52:30.711950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `13`; crypto_alt avg `0.3909` n `239`; crypto_major avg `0.4088` n `8`; equity avg `0.3121` n `160`; fx avg `-0.003` n `6`; index avg `0.0209` n `27`; metal avg `0.0471` n `20`; unknown avg `0.6113` n `1262`
- 1h: commodity avg `0.105` n `13`; crypto_alt avg `-0.2326` n `239`; crypto_major avg `0.0585` n `8`; equity avg `0.2066` n `160`; fx avg `-0.0049` n `6`; index avg `0.0334` n `27`; metal avg `0.05` n `20`; unknown avg `0.4542` n `1256`
- 4h: commodity avg `0.4614` n `13`; crypto_alt avg `-0.0965` n `239`; crypto_major avg `0.7138` n `8`; equity avg `-0.2733` n `160`; fx avg `0.0132` n `6`; index avg `-0.0173` n `27`; metal avg `-0.0272` n `20`; unknown avg `-0.477` n `1250`
- 24h: commodity avg `0.3293` n `13`; crypto_alt avg `-1.8741` n `239`; crypto_major avg `-2.7382` n `8`; equity avg `-1.7121` n `160`; fx avg `-0.0613` n `6`; index avg `-0.1893` n `27`; metal avg `-0.6032` n `20`; unknown avg `0.2382` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2522`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
