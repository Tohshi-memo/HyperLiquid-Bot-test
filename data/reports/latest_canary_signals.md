# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T12:37:25.357085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0962` n `12`; crypto_alt avg `0.1654` n `228`; crypto_major avg `0.1378` n `8`; equity avg `-0.0112` n `69`; fx avg `0.0071` n `6`; index avg `0.0467` n `23`; metal avg `0.0993` n `18`; unknown avg `0.135` n `422`
- 1h: commodity avg `-0.5963` n `12`; crypto_alt avg `-0.1913` n `228`; crypto_major avg `-0.1505` n `8`; equity avg `-0.2499` n `69`; fx avg `0.0127` n `6`; index avg `-0.0967` n `23`; metal avg `-0.1742` n `18`; unknown avg `0.2015` n `422`
- 4h: commodity avg `-1.1155` n `12`; crypto_alt avg `0.144` n `228`; crypto_major avg `0.423` n `8`; equity avg `-0.1516` n `69`; fx avg `0.0141` n `6`; index avg `-0.0313` n `23`; metal avg `0.2135` n `18`; unknown avg `1.6372` n `416`
- 24h: commodity avg `0.1076` n `12`; crypto_alt avg `-0.7498` n `228`; crypto_major avg `-0.7378` n `8`; equity avg `-0.5497` n `69`; fx avg `0.0052` n `6`; index avg `0.4511` n `23`; metal avg `0.1588` n `18`; unknown avg `3.4624` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2891`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
