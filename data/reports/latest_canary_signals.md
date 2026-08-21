# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T14:07:27.869237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.0695` n `230`; crypto_major avg `-0.4355` n `8`; equity avg `-0.1577` n `121`; fx avg `0.0034` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0947` n `793`
- 1h: commodity avg `-0.0545` n `12`; crypto_alt avg `0.0825` n `230`; crypto_major avg `0.1013` n `8`; equity avg `-0.3434` n `121`; fx avg `-0.0002` n `6`; index avg `-0.1058` n `25`; metal avg `-0.028` n `20`; unknown avg `1.1839` n `793`
- 4h: commodity avg `-0.1067` n `12`; crypto_alt avg `1.6819` n `230`; crypto_major avg `0.0539` n `8`; equity avg `-0.3967` n `121`; fx avg `-0.0096` n `6`; index avg `-0.0859` n `25`; metal avg `0.0277` n `20`; unknown avg `1.3502` n `793`
- 24h: commodity avg `0.0463` n `12`; crypto_alt avg `7.9989` n `230`; crypto_major avg `6.2496` n `8`; equity avg `1.2077` n `121`; fx avg `-0.0989` n `6`; index avg `0.0414` n `25`; metal avg `0.8703` n `20`; unknown avg `3.4959` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2338`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1933`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
