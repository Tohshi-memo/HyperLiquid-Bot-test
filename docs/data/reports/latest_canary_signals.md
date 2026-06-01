# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T02:52:23.590823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0889` n `12`; crypto_alt avg `0.5051` n `228`; crypto_major avg `0.3305` n `8`; equity avg `-0.1829` n `69`; fx avg `0.0138` n `6`; index avg `1.1545` n `23`; metal avg `-0.2145` n `18`; unknown avg `0.426` n `422`
- 1h: commodity avg `-0.1483` n `12`; crypto_alt avg `0.7883` n `228`; crypto_major avg `0.5984` n `8`; equity avg `0.0126` n `69`; fx avg `0.0275` n `6`; index avg `0.2879` n `23`; metal avg `-0.0523` n `18`; unknown avg `0.5148` n `421`
- 4h: commodity avg `0.137` n `12`; crypto_alt avg `0.5905` n `228`; crypto_major avg `-0.2022` n `8`; equity avg `-0.0667` n `69`; fx avg `0.104` n `6`; index avg `0.3619` n `23`; metal avg `0.2454` n `18`; unknown avg `-0.3732` n `421`
- 24h: commodity avg `0.8947` n `12`; crypto_alt avg `1.2962` n `228`; crypto_major avg `-0.1035` n `8`; equity avg `0.4894` n `69`; fx avg `0.0584` n `6`; index avg `0.6718` n `23`; metal avg `0.2547` n `18`; unknown avg `1.6173` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2842`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2488`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
