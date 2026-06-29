# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T08:37:29.259131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.0403` n `228`; crypto_major avg `-0.0391` n `8`; equity avg `-0.0085` n `88`; fx avg `0.0005` n `6`; index avg `0.0029` n `23`; metal avg `0.0172` n `20`; unknown avg `0.483` n `764`
- 1h: commodity avg `0.0325` n `12`; crypto_alt avg `-0.3378` n `228`; crypto_major avg `-0.2548` n `8`; equity avg `0.1878` n `88`; fx avg `0.0072` n `6`; index avg `0.0179` n `23`; metal avg `0.0336` n `20`; unknown avg `1.1911` n `764`
- 4h: commodity avg `-0.1392` n `12`; crypto_alt avg `0.0987` n `228`; crypto_major avg `0.1542` n `8`; equity avg `0.7741` n `88`; fx avg `0.0244` n `6`; index avg `0.2316` n `23`; metal avg `0.1204` n `20`; unknown avg `1.5073` n `732`
- 24h: commodity avg `-0.4544` n `12`; crypto_alt avg `0.05` n `228`; crypto_major avg `-0.245` n `8`; equity avg `0.5179` n `88`; fx avg `0.0717` n `6`; index avg `0.0945` n `23`; metal avg `-0.1586` n `20`; unknown avg `-0.2259` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
