# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T00:37:30.397985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1066` n `12`; crypto_alt avg `0.112` n `230`; crypto_major avg `0.0398` n `8`; equity avg `-0.0724` n `102`; fx avg `0.0041` n `6`; index avg `-0.0154` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.0179` n `781`
- 1h: commodity avg `-0.1236` n `12`; crypto_alt avg `0.3005` n `230`; crypto_major avg `0.0264` n `8`; equity avg `0.0042` n `102`; fx avg `-0.0132` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0203` n `20`; unknown avg `5.5385` n `781`
- 4h: commodity avg `0.5018` n `12`; crypto_alt avg `0.2476` n `230`; crypto_major avg `-0.1209` n `8`; equity avg `-0.3288` n `102`; fx avg `-0.0334` n `6`; index avg `-0.0937` n `25`; metal avg `-0.0628` n `20`; unknown avg `2.8012` n `780`
- 24h: commodity avg `0.6218` n `12`; crypto_alt avg `-0.2667` n `230`; crypto_major avg `-2.15` n `8`; equity avg `-2.5151` n `102`; fx avg `-0.06` n `6`; index avg `-0.2992` n `25`; metal avg `-0.3823` n `20`; unknown avg `2.6528` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
