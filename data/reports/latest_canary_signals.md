# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T10:37:28.849740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0646` n `12`; crypto_alt avg `-0.0408` n `230`; crypto_major avg `0.0509` n `8`; equity avg `-0.079` n `100`; fx avg `0.0041` n `6`; index avg `-0.0221` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0126` n `773`
- 1h: commodity avg `0.1921` n `12`; crypto_alt avg `-0.2353` n `230`; crypto_major avg `-0.051` n `8`; equity avg `-0.022` n `100`; fx avg `-0.0134` n `6`; index avg `-0.0127` n `25`; metal avg `0.0601` n `20`; unknown avg `-0.0213` n `773`
- 4h: commodity avg `-0.1928` n `12`; crypto_alt avg `-0.5097` n `230`; crypto_major avg `-0.2755` n `8`; equity avg `0.5096` n `100`; fx avg `-0.0613` n `6`; index avg `0.1073` n `25`; metal avg `0.2826` n `20`; unknown avg `0.2088` n `772`
- 24h: commodity avg `-0.2018` n `12`; crypto_alt avg `-1.335` n `230`; crypto_major avg `-1.7875` n `8`; equity avg `-1.82` n `99`; fx avg `-0.1385` n `6`; index avg `-0.4745` n `25`; metal avg `-0.3018` n `20`; unknown avg `0.1759` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0978`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
