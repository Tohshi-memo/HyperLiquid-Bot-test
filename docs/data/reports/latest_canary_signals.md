# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T20:02:53.421995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0117` n `229`; crypto_major avg `0.0612` n `8`; equity avg `0.0335` n `88`; fx avg `-0.0011` n `6`; index avg `0.0033` n `25`; metal avg `0.0014` n `20`; unknown avg `4.1233` n `765`
- 1h: commodity avg `0.0011` n `12`; crypto_alt avg `-0.0769` n `229`; crypto_major avg `-0.0912` n `8`; equity avg `0.0967` n `88`; fx avg `-0.0471` n `6`; index avg `0.0232` n `25`; metal avg `0.0195` n `20`; unknown avg `0.7644` n `765`
- 4h: commodity avg `-0.0432` n `12`; crypto_alt avg `-0.2217` n `229`; crypto_major avg `-0.006` n `8`; equity avg `0.0229` n `88`; fx avg `-0.0576` n `6`; index avg `-0.0044` n `25`; metal avg `0.0162` n `20`; unknown avg `-0.7131` n `765`
- 24h: commodity avg `-0.0007` n `12`; crypto_alt avg `0.7309` n `229`; crypto_major avg `0.9319` n `8`; equity avg `0.3114` n `88`; fx avg `-0.0585` n `6`; index avg `-0.0318` n `25`; metal avg `0.0818` n `20`; unknown avg `0.4897` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
