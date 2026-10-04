# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T07:22:31.129364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `13`; crypto_alt avg `0.008` n `235`; crypto_major avg `-0.0225` n `8`; equity avg `-0.0162` n `143`; fx avg `-0.0007` n `6`; index avg `-0.0048` n `26`; metal avg `0.0024` n `20`; unknown avg `0.0347` n `1079`
- 1h: commodity avg `-0.0083` n `13`; crypto_alt avg `0.171` n `235`; crypto_major avg `0.0877` n `8`; equity avg `-0.0276` n `143`; fx avg `0.0023` n `6`; index avg `-0.003` n `26`; metal avg `0.0002` n `20`; unknown avg `0.1653` n `1077`
- 4h: commodity avg `0.0074` n `13`; crypto_alt avg `0.6306` n `235`; crypto_major avg `0.3096` n `8`; equity avg `0.026` n `143`; fx avg `-0.0178` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.3631` n `1043`
- 24h: commodity avg `0.1504` n `13`; crypto_alt avg `2.3749` n `235`; crypto_major avg `1.0879` n `8`; equity avg `0.2274` n `143`; fx avg `-0.0426` n `6`; index avg `0.0153` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.4658` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
