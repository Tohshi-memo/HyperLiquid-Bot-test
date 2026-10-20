# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T14:52:33.545049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3093` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.2448` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2149` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.6052` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0156` n `13`; crypto_alt avg `-0.3587` n `237`; crypto_major avg `-0.3064` n `8`; equity avg `-0.0107` n `151`; fx avg `-0.0076` n `6`; index avg `0.0058` n `26`; metal avg `-0.0541` n `20`; unknown avg `0.6356` n `1199`
- 1h: commodity avg `-0.4323` n `13`; crypto_alt avg `2.3162` n `237`; crypto_major avg `1.8125` n `8`; equity avg `2.2661` n `151`; fx avg `0.0018` n `6`; index avg `0.3075` n `26`; metal avg `0.2073` n `20`; unknown avg `1.4847` n `1140`
- 4h: commodity avg `-0.8258` n `13`; crypto_alt avg `3.2748` n `237`; crypto_major avg `2.4835` n `8`; equity avg `2.3351` n `151`; fx avg `0.0627` n `6`; index avg `0.3802` n `26`; metal avg `0.2686` n `20`; unknown avg `3.7052` n `1100`
- 24h: commodity avg `-0.4019` n `13`; crypto_alt avg `3.0867` n `237`; crypto_major avg `1.8366` n `8`; equity avg `0.1359` n `151`; fx avg `0.0302` n `6`; index avg `0.0647` n `26`; metal avg `0.1643` n `20`; unknown avg `3.9233` n `1043`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
