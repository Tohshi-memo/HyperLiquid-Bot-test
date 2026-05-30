# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T15:52:22.333526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0846` n `12`; crypto_alt avg `0.1837` n `228`; crypto_major avg `0.1962` n `8`; equity avg `0.0139` n `69`; fx avg `0.0` n `6`; index avg `0.0075` n `23`; metal avg `0.0008` n `18`; unknown avg `0.2041` n `421`
- 1h: commodity avg `-0.02` n `12`; crypto_alt avg `0.0025` n `228`; crypto_major avg `0.0809` n `8`; equity avg `-0.0694` n `69`; fx avg `0.0007` n `6`; index avg `-0.1123` n `23`; metal avg `0.0252` n `18`; unknown avg `0.05` n `421`
- 4h: commodity avg `0.1992` n `12`; crypto_alt avg `0.1868` n `228`; crypto_major avg `0.5813` n `8`; equity avg `0.2864` n `69`; fx avg `0.0257` n `6`; index avg `0.0672` n `23`; metal avg `-0.0061` n `18`; unknown avg `0.4864` n `421`
- 24h: commodity avg `0.1406` n `12`; crypto_alt avg `0.7408` n `228`; crypto_major avg `1.8274` n `8`; equity avg `1.0951` n `69`; fx avg `-0.0022` n `6`; index avg `0.2112` n `23`; metal avg `-0.2338` n `18`; unknown avg `0.4599` n `400`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
