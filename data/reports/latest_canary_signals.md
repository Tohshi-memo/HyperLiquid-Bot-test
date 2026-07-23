# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T12:22:28.711956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0868` n `12`; crypto_alt avg `0.0846` n `230`; crypto_major avg `0.0798` n `8`; equity avg `-0.2315` n `99`; fx avg `-0.0093` n `6`; index avg `-0.0584` n `25`; metal avg `-0.0899` n `20`; unknown avg `0.0384` n `772`
- 1h: commodity avg `0.0979` n `12`; crypto_alt avg `-0.0127` n `230`; crypto_major avg `-0.1135` n `8`; equity avg `-0.6203` n `99`; fx avg `0.0069` n `6`; index avg `-0.1336` n `25`; metal avg `-0.114` n `20`; unknown avg `0.0487` n `772`
- 4h: commodity avg `0.2649` n `12`; crypto_alt avg `0.1021` n `230`; crypto_major avg `0.2072` n `8`; equity avg `-0.6402` n `99`; fx avg `-0.0272` n `6`; index avg `-0.1345` n `25`; metal avg `-0.1904` n `20`; unknown avg `0.0336` n `772`
- 24h: commodity avg `0.8433` n `12`; crypto_alt avg `-0.0393` n `230`; crypto_major avg `0.1883` n `8`; equity avg `0.44` n `99`; fx avg `-0.0905` n `6`; index avg `0.1092` n `25`; metal avg `-0.6058` n `20`; unknown avg `10.313` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0711`, n `666`, weak_sample_signal
