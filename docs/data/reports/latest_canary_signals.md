# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T17:07:26.734904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.61` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `0.3571` n `228`; crypto_major avg `0.5007` n `8`; equity avg `0.2308` n `88`; fx avg `0.0005` n `6`; index avg `0.044` n `23`; metal avg `0.0364` n `20`; unknown avg `0.0032` n `765`
- 1h: commodity avg `-0.0241` n `12`; crypto_alt avg `0.3784` n `228`; crypto_major avg `0.6256` n `8`; equity avg `0.4451` n `88`; fx avg `-0.0043` n `6`; index avg `0.0666` n `23`; metal avg `-0.1699` n `20`; unknown avg `1.4084` n `765`
- 4h: commodity avg `0.1537` n `12`; crypto_alt avg `0.1233` n `228`; crypto_major avg `0.3983` n `8`; equity avg `0.5114` n `88`; fx avg `0.0342` n `6`; index avg `0.052` n `23`; metal avg `-0.3511` n `20`; unknown avg `0.6554` n `764`
- 24h: commodity avg `-0.6124` n `12`; crypto_alt avg `0.8795` n `228`; crypto_major avg `1.3621` n `8`; equity avg `1.0962` n `88`; fx avg `0.1505` n `6`; index avg `0.1338` n `23`; metal avg `-0.6326` n `20`; unknown avg `3.7175` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
