# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T00:22:26.527088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0761` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.9742` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.8702` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.9349` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.2696` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0187` n `13`; crypto_alt avg `-0.1552` n `235`; crypto_major avg `-0.1719` n `8`; equity avg `0.1084` n `151`; fx avg `-0.0321` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.1388` n `1135`
- 1h: commodity avg `-0.0776` n `13`; crypto_alt avg `-1.5321` n `235`; crypto_major avg `-1.4012` n `8`; equity avg `-0.7195` n `151`; fx avg `-0.0026` n `6`; index avg `-0.1316` n `26`; metal avg `-0.1031` n `20`; unknown avg `1.8451` n `1127`
- 4h: commodity avg `0.0401` n `13`; crypto_alt avg `-3.4314` n `235`; crypto_major avg `-3.036` n `8`; equity avg `-1.1011` n `151`; fx avg `-0.0025` n `6`; index avg `-0.1658` n `26`; metal avg `-0.0618` n `20`; unknown avg `4.235` n `1080`
- 24h: commodity avg `0.65` n `13`; crypto_alt avg `-6.2764` n `235`; crypto_major avg `-4.5836` n `8`; equity avg `-4.7046` n `151`; fx avg `-0.1493` n `6`; index avg `-0.5378` n `26`; metal avg `-0.3427` n `20`; unknown avg `0.6873` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.206`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1829`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1203`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0831`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.082`, n `666`, weak_sample_signal
