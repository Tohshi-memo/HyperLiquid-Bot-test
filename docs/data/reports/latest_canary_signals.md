# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T03:22:24.849505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.1033` n `229`; crypto_major avg `0.0402` n `8`; equity avg `-0.0256` n `92`; fx avg `0.0` n `6`; index avg `0.0033` n `25`; metal avg `0.0329` n `20`; unknown avg `-0.0038` n `765`
- 1h: commodity avg `0.0224` n `12`; crypto_alt avg `0.1493` n `229`; crypto_major avg `0.1756` n `8`; equity avg `0.0254` n `92`; fx avg `0.005` n `6`; index avg `0.0154` n `25`; metal avg `0.04` n `20`; unknown avg `-0.1036` n `765`
- 4h: commodity avg `-0.0303` n `12`; crypto_alt avg `0.0656` n `229`; crypto_major avg `-0.1417` n `8`; equity avg `0.065` n `92`; fx avg `0.0027` n `6`; index avg `0.0022` n `25`; metal avg `0.0389` n `20`; unknown avg `3.228` n `765`
- 24h: commodity avg `-0.3646` n `12`; crypto_alt avg `0.4659` n `229`; crypto_major avg `-0.0343` n `8`; equity avg `-0.8173` n `92`; fx avg `-0.1679` n `6`; index avg `0.0053` n `25`; metal avg `-0.0388` n `20`; unknown avg `3.1711` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
