# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T20:18:13.782820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0297` n `12`; crypto_alt avg `0.032` n `230`; crypto_major avg `0.0708` n `8`; equity avg `0.1096` n `100`; fx avg `-0.0044` n `6`; index avg `0.017` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.0064` n `774`
- 1h: commodity avg `0.1093` n `12`; crypto_alt avg `0.0749` n `230`; crypto_major avg `0.0137` n `8`; equity avg `0.223` n `100`; fx avg `-0.0087` n `6`; index avg `0.0271` n `25`; metal avg `0.0073` n `20`; unknown avg `0.0395` n `773`
- 4h: commodity avg `0.179` n `12`; crypto_alt avg `-0.0058` n `230`; crypto_major avg `-0.0444` n `8`; equity avg `-1.5199` n `100`; fx avg `-0.0379` n `6`; index avg `-0.2822` n `25`; metal avg `-0.256` n `20`; unknown avg `-0.0987` n `773`
- 24h: commodity avg `-0.3226` n `12`; crypto_alt avg `-1.1949` n `230`; crypto_major avg `-1.0878` n `8`; equity avg `-3.5145` n `100`; fx avg `-0.1663` n `6`; index avg `-0.5094` n `25`; metal avg `-0.0264` n `20`; unknown avg `13.8185` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1298`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1248`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1156`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1121`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `666`, weak_sample_signal
