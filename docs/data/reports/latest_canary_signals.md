# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T06:52:35.326948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.0153` n `229`; crypto_major avg `-0.0162` n `8`; equity avg `0.0164` n `91`; fx avg `0.0117` n `6`; index avg `-0.0023` n `25`; metal avg `0.0054` n `20`; unknown avg `0.1708` n `764`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `0.3765` n `229`; crypto_major avg `0.2302` n `8`; equity avg `0.4709` n `91`; fx avg `0.0774` n `6`; index avg `0.069` n `25`; metal avg `0.2881` n `20`; unknown avg `0.1533` n `748`
- 4h: commodity avg `-0.2366` n `12`; crypto_alt avg `1.3569` n `229`; crypto_major avg `1.3805` n `8`; equity avg `0.7276` n `91`; fx avg `0.0749` n `6`; index avg `0.17` n `25`; metal avg `0.4974` n `20`; unknown avg `0.1552` n `748`
- 24h: commodity avg `0.0452` n `12`; crypto_alt avg `0.9087` n `229`; crypto_major avg `0.4354` n `8`; equity avg `1.7407` n `91`; fx avg `0.2096` n `6`; index avg `0.1722` n `25`; metal avg `-0.5929` n `20`; unknown avg `0.4372` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
