# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T22:41:48.131055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.1452` n `229`; crypto_major avg `-0.1434` n `8`; equity avg `-0.0268` n `91`; fx avg `0.0092` n `6`; index avg `-0.0133` n `25`; metal avg `0.02` n `20`; unknown avg `-0.0056` n `763`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `-0.1505` n `229`; crypto_major avg `-0.077` n `8`; equity avg `0.0339` n `91`; fx avg `0.0255` n `6`; index avg `0.0136` n `25`; metal avg `0.017` n `20`; unknown avg `-0.2623` n `763`
- 4h: commodity avg `0.0505` n `12`; crypto_alt avg `0.2419` n `229`; crypto_major avg `0.372` n `8`; equity avg `0.1641` n `91`; fx avg `0.0143` n `6`; index avg `0.0373` n `25`; metal avg `-0.045` n `20`; unknown avg `-0.3632` n `763`
- 24h: commodity avg `0.1838` n `12`; crypto_alt avg `0.5972` n `229`; crypto_major avg `0.0818` n `8`; equity avg `-0.7382` n `90`; fx avg `0.1342` n `6`; index avg `0.0613` n `25`; metal avg `-0.2884` n `20`; unknown avg `-0.4158` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
