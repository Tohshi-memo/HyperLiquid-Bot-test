# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T07:22:30.281117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `0.2308` n `230`; crypto_major avg `0.3298` n `8`; equity avg `0.2961` n `100`; fx avg `0.0012` n `6`; index avg `0.0632` n `25`; metal avg `0.0739` n `20`; unknown avg `0.0083` n `772`
- 1h: commodity avg `-0.121` n `12`; crypto_alt avg `0.3116` n `230`; crypto_major avg `0.5454` n `8`; equity avg `0.3873` n `100`; fx avg `0.0158` n `6`; index avg `0.0911` n `25`; metal avg `0.1526` n `20`; unknown avg `0.0922` n `772`
- 4h: commodity avg `-0.2997` n `12`; crypto_alt avg `0.5463` n `230`; crypto_major avg `0.6885` n `8`; equity avg `0.4908` n `100`; fx avg `0.0479` n `6`; index avg `0.1085` n `25`; metal avg `0.2183` n `20`; unknown avg `0.2326` n `756`
- 24h: commodity avg `0.0153` n `12`; crypto_alt avg `-0.3011` n `230`; crypto_major avg `-0.6268` n `8`; equity avg `-1.3713` n `99`; fx avg `-0.0949` n `6`; index avg `-0.423` n `25`; metal avg `-0.5715` n `20`; unknown avg `0.0886` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.103`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0893`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0858`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0838`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
