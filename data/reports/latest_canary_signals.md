# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T13:22:29.688683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.024` n `230`; crypto_major avg `-0.0504` n `8`; equity avg `0.0506` n `96`; fx avg `0.0006` n `6`; index avg `0.0063` n `25`; metal avg `0.0093` n `20`; unknown avg `0.0082` n `770`
- 1h: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.0269` n `230`; crypto_major avg `-0.0842` n `8`; equity avg `0.11` n `96`; fx avg `-0.0007` n `6`; index avg `0.006` n `25`; metal avg `0.0197` n `20`; unknown avg `-0.0081` n `770`
- 4h: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.0968` n `230`; crypto_major avg `-0.1865` n `8`; equity avg `-0.0449` n `96`; fx avg `0.0059` n `6`; index avg `-0.0181` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.0054` n `770`
- 24h: commodity avg `0.2221` n `12`; crypto_alt avg `0.5243` n `230`; crypto_major avg `1.0863` n `8`; equity avg `0.358` n `96`; fx avg `-0.0129` n `6`; index avg `-0.0298` n `25`; metal avg `-0.067` n `20`; unknown avg `0.1586` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1195`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0879`, n `666`, weak_sample_signal
