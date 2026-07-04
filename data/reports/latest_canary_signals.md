# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T07:37:30.109072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `-0.2091` n `229`; crypto_major avg `-0.1073` n `8`; equity avg `-0.0575` n `88`; fx avg `-0.017` n `6`; index avg `-0.0266` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0312` n `765`
- 1h: commodity avg `0.0006` n `12`; crypto_alt avg `-0.1844` n `229`; crypto_major avg `-0.0558` n `8`; equity avg `-0.0775` n `88`; fx avg `-0.0043` n `6`; index avg `-0.0339` n `25`; metal avg `-0.0138` n `20`; unknown avg `0.0741` n `765`
- 4h: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.616` n `229`; crypto_major avg `-0.2936` n `8`; equity avg `-0.0339` n `88`; fx avg `-0.0056` n `6`; index avg `-0.0264` n `25`; metal avg `0.0206` n `20`; unknown avg `0.0324` n `745`
- 24h: commodity avg `-0.073` n `12`; crypto_alt avg `1.4771` n `229`; crypto_major avg `2.2296` n `8`; equity avg `0.3326` n `88`; fx avg `-0.0063` n `6`; index avg `-0.0503` n `25`; metal avg `-0.187` n `20`; unknown avg `5.0571` n `733`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
