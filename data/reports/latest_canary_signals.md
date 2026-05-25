# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T23:22:13.835679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.0514` n `228`; crypto_major avg `0.058` n `8`; equity avg `-0.0294` n `67`; fx avg `0.0052` n `6`; index avg `-0.0464` n `23`; metal avg `-0.0401` n `18`; unknown avg `-0.1528` n `405`
- 1h: commodity avg `0.1945` n `12`; crypto_alt avg `-0.4489` n `228`; crypto_major avg `-0.2554` n `8`; equity avg `-0.2767` n `67`; fx avg `0.004` n `6`; index avg `-0.1602` n `23`; metal avg `0.0385` n `18`; unknown avg `0.2252` n `405`
- 4h: commodity avg `0.15` n `12`; crypto_alt avg `-1.0332` n `228`; crypto_major avg `-0.4766` n `8`; equity avg `-0.2189` n `67`; fx avg `0.0387` n `6`; index avg `-0.1623` n `23`; metal avg `0.1038` n `18`; unknown avg `-0.5969` n `405`
- 24h: commodity avg `-0.2674` n `12`; crypto_alt avg `1.7078` n `228`; crypto_major avg `0.018` n `8`; equity avg `0.7035` n `67`; fx avg `-0.0638` n `6`; index avg `0.4618` n `23`; metal avg `0.3393` n `18`; unknown avg `0.8289` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
