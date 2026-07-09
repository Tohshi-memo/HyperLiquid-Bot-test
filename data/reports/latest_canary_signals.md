# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T04:09:35.999074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.0973` n `229`; crypto_major avg `0.0327` n `8`; equity avg `0.0499` n `91`; fx avg `-0.0029` n `6`; index avg `0.0036` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0476` n `764`
- 1h: commodity avg `-0.0222` n `12`; crypto_alt avg `0.3147` n `229`; crypto_major avg `0.3433` n `8`; equity avg `0.2626` n `91`; fx avg `-0.0108` n `6`; index avg `0.1087` n `25`; metal avg `0.0433` n `20`; unknown avg `-0.0153` n `764`
- 4h: commodity avg `0.0052` n `12`; crypto_alt avg `-0.1488` n `229`; crypto_major avg `-0.2037` n `8`; equity avg `-0.3302` n `91`; fx avg `0.0223` n `6`; index avg `-0.1096` n `25`; metal avg `-0.1634` n `20`; unknown avg `-0.4493` n `764`
- 24h: commodity avg `0.323` n `12`; crypto_alt avg `-0.242` n `229`; crypto_major avg `-0.8025` n `8`; equity avg `0.4801` n `91`; fx avg `0.0213` n `6`; index avg `-0.1029` n `25`; metal avg `-1.0396` n `20`; unknown avg `0.0548` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1011`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0934`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0777`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0666`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0642`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0638`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0605`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.06`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0574`, n `669`, weak_sample_signal
