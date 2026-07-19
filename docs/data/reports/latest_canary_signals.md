# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T06:07:27.254011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.0518` n `230`; crypto_major avg `-0.0749` n `8`; equity avg `-0.0306` n `96`; fx avg `0.0028` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0084` n `752`
- 1h: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.0699` n `230`; crypto_major avg `-0.0715` n `8`; equity avg `-0.0227` n `96`; fx avg `0.0082` n `6`; index avg `0.0024` n `25`; metal avg `0.0036` n `20`; unknown avg `0.0118` n `752`
- 4h: commodity avg `-0.0261` n `12`; crypto_alt avg `-0.2965` n `230`; crypto_major avg `-0.2644` n `8`; equity avg `0.0153` n `96`; fx avg `-0.003` n `6`; index avg `0.0093` n `25`; metal avg `0.0093` n `20`; unknown avg `-0.0234` n `752`
- 24h: commodity avg `0.3417` n `12`; crypto_alt avg `0.2301` n `230`; crypto_major avg `1.0512` n `8`; equity avg `-0.0129` n `96`; fx avg `-0.0106` n `6`; index avg `-0.0544` n `25`; metal avg `-0.0275` n `20`; unknown avg `-0.011` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
