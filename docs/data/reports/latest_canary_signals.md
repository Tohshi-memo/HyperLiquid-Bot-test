# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T01:37:27.237967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2614` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.0306` n `229`; crypto_major avg `-0.0376` n `8`; equity avg `0.0285` n `88`; fx avg `0.0001` n `6`; index avg `-0.0343` n `25`; metal avg `0.0105` n `20`; unknown avg `0.7123` n `765`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `-0.3856` n `229`; crypto_major avg `-0.4104` n `8`; equity avg `-0.0073` n `88`; fx avg `0.0063` n `6`; index avg `-0.0303` n `25`; metal avg `0.0116` n `20`; unknown avg `0.1037` n `763`
- 4h: commodity avg `0.0362` n `12`; crypto_alt avg `-1.3274` n `229`; crypto_major avg `-1.2834` n `8`; equity avg `-0.0209` n `88`; fx avg `0.0169` n `6`; index avg `-0.022` n `25`; metal avg `0.0008` n `20`; unknown avg `0.1622` n `763`
- 24h: commodity avg `0.0203` n `12`; crypto_alt avg `-0.1266` n `229`; crypto_major avg `-0.1906` n `8`; equity avg `0.2749` n `88`; fx avg `0.0048` n `6`; index avg `0.0142` n `25`; metal avg `0.1314` n `20`; unknown avg `-0.7762` n `739`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
