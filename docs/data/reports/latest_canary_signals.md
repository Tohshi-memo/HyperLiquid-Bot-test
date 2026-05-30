# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T22:22:22.879093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0568` n `12`; crypto_alt avg `-0.0238` n `228`; crypto_major avg `0.0955` n `8`; equity avg `0.0103` n `69`; fx avg `0.002` n `6`; index avg `0.023` n `23`; metal avg `0.0136` n `18`; unknown avg `-0.0606` n `421`
- 1h: commodity avg `0.1499` n `12`; crypto_alt avg `-0.7332` n `228`; crypto_major avg `-0.436` n `8`; equity avg `-0.0779` n `69`; fx avg `0.0012` n `6`; index avg `-0.0458` n `23`; metal avg `0.0014` n `18`; unknown avg `0.8445` n `421`
- 4h: commodity avg `0.2786` n `12`; crypto_alt avg `-0.4934` n `228`; crypto_major avg `-0.3516` n `8`; equity avg `0.1677` n `69`; fx avg `0.0082` n `6`; index avg `0.0075` n `23`; metal avg `-0.0066` n `18`; unknown avg `0.6878` n `421`
- 24h: commodity avg `0.0398` n `12`; crypto_alt avg `1.1129` n `228`; crypto_major avg `2.3439` n `8`; equity avg `0.9291` n `69`; fx avg `0.0275` n `6`; index avg `0.0733` n `23`; metal avg `0.0592` n `18`; unknown avg `0.2776` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
