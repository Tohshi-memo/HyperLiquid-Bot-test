# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T14:37:25.535613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0542` n `12`; crypto_alt avg `-0.3705` n `228`; crypto_major avg `-0.3081` n `8`; equity avg `0.2305` n `74`; fx avg `-0.0055` n `6`; index avg `0.1079` n `23`; metal avg `-0.0087` n `18`; unknown avg `-0.035` n `424`
- 1h: commodity avg `-0.1493` n `12`; crypto_alt avg `-0.3288` n `228`; crypto_major avg `-0.2729` n `8`; equity avg `0.0653` n `74`; fx avg `0.0047` n `6`; index avg `0.0576` n `23`; metal avg `-0.5929` n `18`; unknown avg `1.0536` n `424`
- 4h: commodity avg `-0.4913` n `12`; crypto_alt avg `1.422` n `228`; crypto_major avg `1.1129` n `8`; equity avg `1.1163` n `73`; fx avg `0.0024` n `6`; index avg `0.3256` n `23`; metal avg `0.2953` n `18`; unknown avg `2.4698` n `422`
- 24h: commodity avg `-0.5591` n `12`; crypto_alt avg `-6.6552` n `228`; crypto_major avg `-4.7752` n `8`; equity avg `-2.3042` n `73`; fx avg `0.1312` n `6`; index avg `-0.8391` n `23`; metal avg `0.042` n `18`; unknown avg `-1.3439` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
