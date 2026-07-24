# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T18:07:37.730910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `-0.0376` n `230`; crypto_major avg `0.0127` n `8`; equity avg `-0.1771` n `100`; fx avg `0.001` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.0169` n `773`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `0.2524` n `230`; crypto_major avg `0.2848` n `8`; equity avg `-0.0069` n `100`; fx avg `-0.0155` n `6`; index avg `0.025` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0654` n `773`
- 4h: commodity avg `-0.2913` n `12`; crypto_alt avg `0.3653` n `230`; crypto_major avg `0.3148` n `8`; equity avg `-0.2122` n `100`; fx avg `-0.0139` n `6`; index avg `0.0625` n `25`; metal avg `0.1231` n `20`; unknown avg `13.3011` n `773`
- 24h: commodity avg `-0.9045` n `12`; crypto_alt avg `-0.6752` n `230`; crypto_major avg `-0.6608` n `8`; equity avg `-2.3798` n `100`; fx avg `-0.1625` n `6`; index avg `-0.2341` n `25`; metal avg `0.1409` n `20`; unknown avg `14.1404` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1216`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1177`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1107`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.103`, n `666`, weak_sample_signal
