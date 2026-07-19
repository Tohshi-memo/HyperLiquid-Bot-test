# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T15:07:26.078303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `-0.0418` n `230`; crypto_major avg `-0.0661` n `8`; equity avg `-0.0582` n `96`; fx avg `-0.0007` n `6`; index avg `-0.0062` n `25`; metal avg `0.0002` n `20`; unknown avg `0.0118` n `770`
- 1h: commodity avg `0.0231` n `12`; crypto_alt avg `0.0243` n `230`; crypto_major avg `0.0733` n `8`; equity avg `-0.0783` n `96`; fx avg `-0.0016` n `6`; index avg `-0.005` n `25`; metal avg `0.0031` n `20`; unknown avg `0.032` n `770`
- 4h: commodity avg `0.0292` n `12`; crypto_alt avg `-0.1488` n `230`; crypto_major avg `-0.0034` n `8`; equity avg `-0.0879` n `96`; fx avg `-0.0051` n `6`; index avg `-0.011` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0295` n `770`
- 24h: commodity avg `0.2254` n `12`; crypto_alt avg `0.4077` n `230`; crypto_major avg `1.0238` n `8`; equity avg `0.2151` n `96`; fx avg `-0.0039` n `6`; index avg `-0.0327` n `25`; metal avg `-0.0456` n `20`; unknown avg `0.1106` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1296`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1253`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
