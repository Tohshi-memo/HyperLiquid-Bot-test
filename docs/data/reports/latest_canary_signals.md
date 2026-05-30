# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T12:37:17.749300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.123` n `228`; crypto_major avg `-0.0466` n `8`; equity avg `0.0462` n `69`; fx avg `0.0149` n `6`; index avg `-0.0033` n `23`; metal avg `0.0194` n `18`; unknown avg `0.2184` n `421`
- 1h: commodity avg `0.1202` n `12`; crypto_alt avg `-0.0696` n `228`; crypto_major avg `0.0345` n `8`; equity avg `0.2277` n `69`; fx avg `0.018` n `6`; index avg `0.0135` n `23`; metal avg `0.0107` n `18`; unknown avg `0.3013` n `421`
- 4h: commodity avg `0.2045` n `12`; crypto_alt avg `0.0298` n `228`; crypto_major avg `0.3384` n `8`; equity avg `0.2597` n `69`; fx avg `0.2186` n `6`; index avg `0.0512` n `23`; metal avg `0.1037` n `18`; unknown avg `0.8895` n `421`
- 24h: commodity avg `-0.3224` n `12`; crypto_alt avg `2.4567` n `228`; crypto_major avg `2.8533` n `8`; equity avg `1.6074` n `69`; fx avg `0.1061` n `6`; index avg `0.0255` n `23`; metal avg `0.1768` n `18`; unknown avg `1.5052` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1917`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
