# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T04:37:25.837476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.018` n `12`; crypto_alt avg `0.0693` n `229`; crypto_major avg `0.1099` n `8`; equity avg `0.114` n `88`; fx avg `-0.0159` n `6`; index avg `0.0548` n `25`; metal avg `-0.0703` n `20`; unknown avg `0.2427` n `765`
- 1h: commodity avg `0.0426` n `12`; crypto_alt avg `-0.1514` n `229`; crypto_major avg `-0.0299` n `8`; equity avg `0.3856` n `88`; fx avg `-0.0263` n `6`; index avg `0.1353` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.3765` n `765`
- 4h: commodity avg `0.2089` n `12`; crypto_alt avg `0.4985` n `229`; crypto_major avg `0.4355` n `8`; equity avg `1.4389` n `88`; fx avg `-0.0343` n `6`; index avg `0.3814` n `25`; metal avg `0.4859` n `20`; unknown avg `0.59` n `761`
- 24h: commodity avg `0.3805` n `12`; crypto_alt avg `1.6105` n `228`; crypto_major avg `2.5401` n `8`; equity avg `-0.431` n `88`; fx avg `-0.0684` n `6`; index avg `0.0171` n `25`; metal avg `1.2205` n `20`; unknown avg `6.5572` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
