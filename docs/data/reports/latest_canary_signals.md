# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T23:37:27.448957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0166` n `13`; crypto_alt avg `0.0106` n `235`; crypto_major avg `-0.0571` n `8`; equity avg `-0.0122` n `143`; fx avg `0.0` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.0505` n `1079`
- 1h: commodity avg `-0.0067` n `13`; crypto_alt avg `0.1663` n `235`; crypto_major avg `-0.132` n `8`; equity avg `0.0128` n `143`; fx avg `-0.0154` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.1253` n `1077`
- 4h: commodity avg `0.0477` n `13`; crypto_alt avg `0.5898` n `235`; crypto_major avg `0.0193` n `8`; equity avg `0.0911` n `143`; fx avg `0.0175` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0046` n `20`; unknown avg `0.3145` n `1054`
- 24h: commodity avg `-0.0353` n `13`; crypto_alt avg `1.9283` n `235`; crypto_major avg `0.5611` n `8`; equity avg `0.1782` n `143`; fx avg `-0.0146` n `6`; index avg `0.0483` n `26`; metal avg `-0.0185` n `20`; unknown avg `0.093` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
