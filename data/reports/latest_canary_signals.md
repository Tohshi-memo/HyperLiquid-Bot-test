# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T18:37:29.910265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.0697` n `229`; crypto_major avg `0.0182` n `8`; equity avg `-0.0465` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0116` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.1571` n `765`
- 1h: commodity avg `-0.0398` n `12`; crypto_alt avg `-0.0144` n `229`; crypto_major avg `0.0794` n `8`; equity avg `0.0018` n `88`; fx avg `0.0039` n `6`; index avg `-0.0174` n `25`; metal avg `-0.0153` n `20`; unknown avg `1.6826` n `765`
- 4h: commodity avg `-0.0405` n `12`; crypto_alt avg `0.4359` n `229`; crypto_major avg `0.6666` n `8`; equity avg `0.1502` n `88`; fx avg `-0.0225` n `6`; index avg `0.0358` n `25`; metal avg `0.0095` n `20`; unknown avg `2.2864` n `765`
- 24h: commodity avg `0.1604` n `12`; crypto_alt avg `2.5199` n `229`; crypto_major avg `2.1588` n `8`; equity avg `2.2245` n `88`; fx avg `-0.0528` n `6`; index avg `0.6237` n `25`; metal avg `0.5264` n `20`; unknown avg `11.8799` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
