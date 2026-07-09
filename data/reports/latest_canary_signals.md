# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T04:29:51.945332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `12`; crypto_alt avg `0.0834` n `229`; crypto_major avg `0.0052` n `8`; equity avg `-0.0673` n `91`; fx avg `-0.0304` n `6`; index avg `-0.0497` n `25`; metal avg `-0.0358` n `20`; unknown avg `-0.2259` n `764`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `0.3398` n `229`; crypto_major avg `0.2255` n `8`; equity avg `0.2297` n `91`; fx avg `-0.0409` n `6`; index avg `0.0541` n `25`; metal avg `0.0356` n `20`; unknown avg `-0.1663` n `764`
- 4h: commodity avg `0.0448` n `12`; crypto_alt avg `0.0567` n `229`; crypto_major avg `-0.0923` n `8`; equity avg `-0.5039` n `91`; fx avg `0.0216` n `6`; index avg `-0.1896` n `25`; metal avg `-0.1771` n `20`; unknown avg `-0.5725` n `764`
- 24h: commodity avg `0.3555` n `12`; crypto_alt avg `-0.263` n `229`; crypto_major avg `-0.9057` n `8`; equity avg `0.5197` n `91`; fx avg `-0.0008` n `6`; index avg `-0.1263` n `25`; metal avg `-1.0723` n `20`; unknown avg `0.0736` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0997`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.077`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0668`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0635`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0621`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0609`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0607`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `669`, weak_sample_signal
