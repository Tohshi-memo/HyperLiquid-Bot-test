# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T15:43:55.153083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0498` n `12`; crypto_alt avg `0.1346` n `230`; crypto_major avg `0.1166` n `8`; equity avg `-0.0341` n `100`; fx avg `0.0237` n `6`; index avg `-0.0151` n `25`; metal avg `-0.0217` n `20`; unknown avg `-0.0699` n `773`
- 1h: commodity avg `-0.2616` n `12`; crypto_alt avg `0.5412` n `230`; crypto_major avg `0.5638` n `8`; equity avg `0.8015` n `100`; fx avg `0.0353` n `6`; index avg `0.1736` n `25`; metal avg `0.1652` n `20`; unknown avg `13.5461` n `773`
- 4h: commodity avg `-0.1156` n `12`; crypto_alt avg `-0.6288` n `230`; crypto_major avg `-0.5385` n `8`; equity avg `-1.798` n `100`; fx avg `0.029` n `6`; index avg `-0.0935` n `25`; metal avg `0.0689` n `20`; unknown avg `13.1006` n `773`
- 24h: commodity avg `-0.6727` n `12`; crypto_alt avg `-1.3003` n `230`; crypto_major avg `-1.1069` n `8`; equity avg `-1.7682` n `100`; fx avg `-0.0999` n `6`; index avg `-0.0989` n `25`; metal avg `0.1812` n `20`; unknown avg `13.568` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.118`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1173`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1039`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1003`, n `666`, weak_sample_signal
