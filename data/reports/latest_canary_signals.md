# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T14:52:28.438382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0339` n `12`; crypto_alt avg `0.0248` n `229`; crypto_major avg `0.0823` n `8`; equity avg `0.0649` n `91`; fx avg `-0.0151` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0251` n `20`; unknown avg `-0.0354` n `765`
- 1h: commodity avg `-0.173` n `12`; crypto_alt avg `-0.2018` n `229`; crypto_major avg `-0.3617` n `8`; equity avg `-0.4994` n `91`; fx avg `-0.0158` n `6`; index avg `-0.0941` n `25`; metal avg `-0.0673` n `20`; unknown avg `-0.0493` n `765`
- 4h: commodity avg `-0.7609` n `12`; crypto_alt avg `0.2201` n `229`; crypto_major avg `0.0932` n `8`; equity avg `0.86` n `91`; fx avg `-0.0397` n `6`; index avg `0.2651` n `25`; metal avg `0.4535` n `20`; unknown avg `0.0551` n `764`
- 24h: commodity avg `-1.1066` n `12`; crypto_alt avg `1.4885` n `229`; crypto_major avg `0.9109` n `8`; equity avg `2.6217` n `91`; fx avg `0.0555` n `6`; index avg `0.4805` n `25`; metal avg `1.0629` n `20`; unknown avg `0.9502` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
