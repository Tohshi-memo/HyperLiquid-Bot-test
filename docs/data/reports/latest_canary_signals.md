# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T03:37:36.231789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.205` n `228`; crypto_major avg `-0.2055` n `8`; equity avg `-0.1389` n `88`; fx avg `0.0036` n `6`; index avg `-0.0547` n `23`; metal avg `-0.1595` n `20`; unknown avg `-0.1796` n `764`
- 1h: commodity avg `0.0487` n `12`; crypto_alt avg `0.7439` n `228`; crypto_major avg `0.5483` n `8`; equity avg `0.1394` n `88`; fx avg `0.0063` n `6`; index avg `-0.0323` n `23`; metal avg `0.1208` n `20`; unknown avg `-0.1285` n `764`
- 4h: commodity avg `0.0631` n `12`; crypto_alt avg `0.9989` n `228`; crypto_major avg `0.5746` n `8`; equity avg `-0.5758` n `88`; fx avg `0.114` n `6`; index avg `-0.2527` n `23`; metal avg `0.1062` n `20`; unknown avg `0.1857` n `764`
- 24h: commodity avg `-0.299` n `12`; crypto_alt avg `0.441` n `228`; crypto_major avg `0.1884` n `8`; equity avg `-0.0919` n `88`; fx avg `0.0503` n `6`; index avg `-0.1037` n `23`; metal avg `-0.1286` n `20`; unknown avg `-0.7462` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.21`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
