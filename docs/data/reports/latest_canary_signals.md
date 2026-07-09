# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T12:08:19.640878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `0.0365` n `229`; crypto_major avg `0.0791` n `8`; equity avg `0.0484` n `91`; fx avg `0.0095` n `6`; index avg `-0.0006` n `25`; metal avg `0.122` n `20`; unknown avg `0.0084` n `764`
- 1h: commodity avg `0.044` n `12`; crypto_alt avg `0.0794` n `229`; crypto_major avg `0.0242` n `8`; equity avg `0.5201` n `91`; fx avg `0.0037` n `6`; index avg `0.1304` n `25`; metal avg `0.2125` n `20`; unknown avg `0.0245` n `764`
- 4h: commodity avg `0.3305` n `12`; crypto_alt avg `-0.1824` n `229`; crypto_major avg `-0.4389` n `8`; equity avg `0.0432` n `91`; fx avg `-0.0266` n `6`; index avg `0.0426` n `25`; metal avg `0.1035` n `20`; unknown avg `-0.0418` n `764`
- 24h: commodity avg `-0.2273` n `12`; crypto_alt avg `0.9748` n `229`; crypto_major avg `0.0018` n `8`; equity avg `2.9211` n `91`; fx avg `0.1436` n `6`; index avg `0.4412` n `25`; metal avg `0.6476` n `20`; unknown avg `0.6662` n `741`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
