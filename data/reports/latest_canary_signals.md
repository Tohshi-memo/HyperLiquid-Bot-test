# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T02:52:27.800190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0418` n `12`; crypto_alt avg `-0.2112` n `229`; crypto_major avg `-0.2529` n `8`; equity avg `-0.3442` n `91`; fx avg `0.0068` n `6`; index avg `-0.1039` n `25`; metal avg `-0.1017` n `20`; unknown avg `-0.041` n `764`
- 1h: commodity avg `0.0828` n `12`; crypto_alt avg `-0.2421` n `229`; crypto_major avg `-0.3174` n `8`; equity avg `-0.649` n `91`; fx avg `-0.0141` n `6`; index avg `-0.1538` n `25`; metal avg `-0.0771` n `20`; unknown avg `-0.2721` n `764`
- 4h: commodity avg `0.0082` n `12`; crypto_alt avg `-0.2095` n `229`; crypto_major avg `-0.4752` n `8`; equity avg `-0.1941` n `91`; fx avg `0.0189` n `6`; index avg `-0.1727` n `25`; metal avg `-0.1237` n `20`; unknown avg `-0.126` n `764`
- 24h: commodity avg `0.3953` n `12`; crypto_alt avg `-0.6447` n `229`; crypto_major avg `-1.4305` n `8`; equity avg `0.5411` n `91`; fx avg `0.0414` n `6`; index avg `-0.1982` n `25`; metal avg `-0.8774` n `20`; unknown avg `0.0219` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
