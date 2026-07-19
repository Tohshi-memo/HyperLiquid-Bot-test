# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T13:07:31.094800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.0209` n `230`; crypto_major avg `-0.1104` n `8`; equity avg `-0.0203` n `96`; fx avg `-0.0013` n `6`; index avg `-0.0009` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0159` n `770`
- 1h: commodity avg `0.0323` n `12`; crypto_alt avg `0.0914` n `230`; crypto_major avg `-0.0464` n `8`; equity avg `0.0306` n `96`; fx avg `-0.0011` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.0198` n `770`
- 4h: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.351` n `230`; crypto_major avg `-0.4032` n `8`; equity avg `-0.1821` n `96`; fx avg `0.0059` n `6`; index avg `-0.0222` n `25`; metal avg `-0.0155` n `20`; unknown avg `-0.0204` n `770`
- 24h: commodity avg `0.2062` n `12`; crypto_alt avg `0.3522` n `230`; crypto_major avg `0.8979` n `8`; equity avg `0.2269` n `96`; fx avg `-0.008` n `6`; index avg `-0.0379` n `25`; metal avg `-0.0814` n `20`; unknown avg `0.1207` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1164`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1152`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0865`, n `666`, weak_sample_signal
