# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T15:26:32.093666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8291` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1397` n `12`; crypto_alt avg `-0.0392` n `230`; crypto_major avg `-0.1235` n `8`; equity avg `-0.1964` n `109`; fx avg `-0.0057` n `6`; index avg `-0.0728` n `25`; metal avg `-0.0918` n `20`; unknown avg `-0.0132` n `784`
- 1h: commodity avg `0.1758` n `12`; crypto_alt avg `0.2263` n `230`; crypto_major avg `0.1446` n `8`; equity avg `0.0302` n `109`; fx avg `-0.04` n `6`; index avg `-0.0499` n `25`; metal avg `-0.0225` n `20`; unknown avg `0.2078` n `781`
- 4h: commodity avg `0.2052` n `12`; crypto_alt avg `0.6058` n `230`; crypto_major avg `0.1435` n `8`; equity avg `1.9726` n `109`; fx avg `0.0023` n `6`; index avg `0.1659` n `25`; metal avg `-0.1355` n `20`; unknown avg `0.6782` n `781`
- 24h: commodity avg `0.358` n `12`; crypto_alt avg `0.6261` n `230`; crypto_major avg `-0.5646` n `8`; equity avg `0.0579` n `109`; fx avg `0.0317` n `6`; index avg `-0.2314` n `25`; metal avg `-0.0271` n `20`; unknown avg `113.3838` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
