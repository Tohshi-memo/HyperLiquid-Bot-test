# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T09:07:27.613159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0294` n `12`; crypto_alt avg `0.2957` n `228`; crypto_major avg `0.2928` n `8`; equity avg `0.1459` n `69`; fx avg `0.0075` n `6`; index avg `0.0421` n `23`; metal avg `0.0225` n `18`; unknown avg `0.8005` n `422`
- 1h: commodity avg `0.0206` n `12`; crypto_alt avg `0.2804` n `228`; crypto_major avg `0.1454` n `8`; equity avg `0.0809` n `69`; fx avg `0.0048` n `6`; index avg `0.0152` n `23`; metal avg `0.0213` n `18`; unknown avg `0.0327` n `422`
- 4h: commodity avg `0.5525` n `12`; crypto_alt avg `-1.2461` n `228`; crypto_major avg `-0.8509` n `8`; equity avg `-0.3962` n `69`; fx avg `-0.025` n `6`; index avg `-0.3302` n `23`; metal avg `-0.2036` n `18`; unknown avg `0.6505` n `412`
- 24h: commodity avg `1.2499` n `12`; crypto_alt avg `-0.3443` n `228`; crypto_major avg `-0.8766` n `8`; equity avg `-0.192` n `69`; fx avg `-0.0106` n `6`; index avg `0.5086` n `23`; metal avg `0.0549` n `18`; unknown avg `1.2386` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2884`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
