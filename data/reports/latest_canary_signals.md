# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T21:52:28.662600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.0391` n `239`; crypto_major avg `-0.1597` n `8`; equity avg `0.0405` n `161`; fx avg `-0.0463` n `6`; index avg `0.0024` n `27`; metal avg `0.0013` n `20`; unknown avg `2.4098` n `1262`
- 1h: commodity avg `0.03` n `13`; crypto_alt avg `-0.4699` n `239`; crypto_major avg `-0.4181` n `8`; equity avg `0.2182` n `161`; fx avg `-0.0497` n `6`; index avg `-0.001` n `27`; metal avg `-0.0342` n `20`; unknown avg `4.1552` n `1218`
- 4h: commodity avg `-0.0699` n `13`; crypto_alt avg `-0.9735` n `239`; crypto_major avg `-0.669` n `8`; equity avg `-0.9553` n `161`; fx avg `-0.0284` n `6`; index avg `-0.0664` n `27`; metal avg `-0.154` n `20`; unknown avg `5.378` n `1210`
- 24h: commodity avg `0.2117` n `13`; crypto_alt avg `0.1407` n `239`; crypto_major avg `0.6608` n `8`; equity avg `4.589` n `161`; fx avg `-0.1958` n `6`; index avg `0.4536` n `27`; metal avg `-0.0859` n `20`; unknown avg `5.0338` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
