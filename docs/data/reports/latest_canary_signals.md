# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T16:22:27.009901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `0.1164` n `230`; crypto_major avg `0.0989` n `8`; equity avg `0.0319` n `96`; fx avg `0.0007` n `6`; index avg `-0.0294` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.0638` n `770`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `0.0114` n `230`; crypto_major avg `-0.0257` n `8`; equity avg `-0.0153` n `96`; fx avg `0.0024` n `6`; index avg `-0.0637` n `25`; metal avg `-0.0264` n `20`; unknown avg `0.0235` n `770`
- 4h: commodity avg `0.0224` n `12`; crypto_alt avg `0.1779` n `230`; crypto_major avg `0.1905` n `8`; equity avg `0.0076` n `96`; fx avg `0.0064` n `6`; index avg `-0.0646` n `25`; metal avg `0.0006` n `20`; unknown avg `0.1098` n `770`
- 24h: commodity avg `0.2188` n `12`; crypto_alt avg `0.5051` n `230`; crypto_major avg `0.9709` n `8`; equity avg `0.294` n `96`; fx avg `0.0414` n `6`; index avg `-0.0825` n `25`; metal avg `-0.0518` n `20`; unknown avg `0.1491` n `752`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1334`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0966`, n `666`, weak_sample_signal
