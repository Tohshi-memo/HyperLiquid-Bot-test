# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T16:52:31.304856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.1098` n `230`; crypto_major avg `-0.1649` n `8`; equity avg `-0.3255` n `100`; fx avg `-0.0145` n `6`; index avg `-0.0663` n `25`; metal avg `-0.0709` n `20`; unknown avg `-0.0602` n `773`
- 1h: commodity avg `-0.1495` n `12`; crypto_alt avg `-0.2213` n `230`; crypto_major avg `-0.338` n `8`; equity avg `-0.3647` n `100`; fx avg `-0.0296` n `6`; index avg `-0.0953` n `25`; metal avg `-0.1116` n `20`; unknown avg `0.021` n `773`
- 4h: commodity avg `-0.3319` n `12`; crypto_alt avg `-0.7476` n `230`; crypto_major avg `-0.8502` n `8`; equity avg `-2.015` n `100`; fx avg `0.0096` n `6`; index avg `-0.1528` n `25`; metal avg `-0.0013` n `20`; unknown avg `13.2429` n `773`
- 24h: commodity avg `-0.6844` n `12`; crypto_alt avg `-1.6309` n `230`; crypto_major avg `-1.3709` n `8`; equity avg `-2.6291` n `100`; fx avg `-0.14` n `6`; index avg `-0.277` n `25`; metal avg `0.0668` n `20`; unknown avg `13.7166` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1454`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1411`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1194`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1194`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1146`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1131`, n `667`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1047`, n `667`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1034`, n `669`, weak_sample_signal
