# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T12:22:29.736079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `0.0954` n `230`; crypto_major avg `-0.0125` n `8`; equity avg `-0.0286` n `96`; fx avg `0.0002` n `6`; index avg `-0.0025` n `25`; metal avg `-0.0131` n `20`; unknown avg `-0.0105` n `770`
- 1h: commodity avg `0.0629` n `12`; crypto_alt avg `-0.3037` n `230`; crypto_major avg `-0.3924` n `8`; equity avg `-0.1347` n `96`; fx avg `-0.0128` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0167` n `20`; unknown avg `-0.0288` n `770`
- 4h: commodity avg `0.0231` n `12`; crypto_alt avg `-0.1843` n `230`; crypto_major avg `-0.1686` n `8`; equity avg `-0.2088` n `96`; fx avg `-0.0172` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0584` n `20`; unknown avg `-0.0603` n `770`
- 24h: commodity avg `0.2133` n `12`; crypto_alt avg `0.3958` n `230`; crypto_major avg `1.005` n `8`; equity avg `0.139` n `96`; fx avg `-0.008` n `6`; index avg `-0.0437` n `25`; metal avg `-0.1032` n `20`; unknown avg `0.1354` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1159`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1146`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
