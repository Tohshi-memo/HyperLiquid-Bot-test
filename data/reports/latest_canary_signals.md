# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T01:37:24.297220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0665` n `12`; crypto_alt avg `-0.0406` n `230`; crypto_major avg `0.0006` n `8`; equity avg `-0.1043` n `102`; fx avg `0.0115` n `6`; index avg `-0.0344` n `25`; metal avg `0.0506` n `20`; unknown avg `-0.0878` n `784`
- 1h: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.4052` n `230`; crypto_major avg `-0.3166` n `8`; equity avg `-0.0224` n `102`; fx avg `-0.0698` n `6`; index avg `-0.0153` n `25`; metal avg `0.0208` n `20`; unknown avg `-0.0681` n `784`
- 4h: commodity avg `-0.1411` n `12`; crypto_alt avg `-0.8343` n `230`; crypto_major avg `-0.7351` n `8`; equity avg `-0.0117` n `102`; fx avg `-0.2798` n `6`; index avg `-0.1744` n `25`; metal avg `-0.2415` n `20`; unknown avg `2.1339` n `783`
- 24h: commodity avg `-0.9377` n `12`; crypto_alt avg `-0.0809` n `230`; crypto_major avg `0.5248` n `8`; equity avg `1.3043` n `102`; fx avg `-0.2737` n `6`; index avg `0.1061` n `25`; metal avg `0.0888` n `20`; unknown avg `1.4615` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
