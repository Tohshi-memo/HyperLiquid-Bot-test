# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T01:22:31.679092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.0472` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.0018` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.8496` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.6353` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4173` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0136` n `13`; crypto_alt avg `-0.3212` n `239`; crypto_major avg `-0.49` n `8`; equity avg `-0.0834` n `162`; fx avg `0.0045` n `6`; index avg `0.0079` n `27`; metal avg `-0.0616` n `20`; unknown avg `2.025` n `1260`
- 1h: commodity avg `0.0112` n `13`; crypto_alt avg `-1.3811` n `239`; crypto_major avg `-2.036` n `8`; equity avg `-0.4007` n `162`; fx avg `0.0032` n `6`; index avg `-0.0342` n `27`; metal avg `-0.1864` n `20`; unknown avg `0.0588` n `1260`
- 4h: commodity avg `0.1337` n `13`; crypto_alt avg `0.1686` n `239`; crypto_major avg `-1.4129` n `8`; equity avg `-0.0378` n `162`; fx avg `0.0092` n `6`; index avg `0.0044` n `27`; metal avg `-0.0818` n `20`; unknown avg `-0.0833` n `1216`
- 24h: commodity avg `-0.0037` n `13`; crypto_alt avg `-8.9838` n `239`; crypto_major avg `-9.3745` n `8`; equity avg `-1.7271` n `162`; fx avg `0.0277` n `6`; index avg `-0.1346` n `27`; metal avg `-0.6189` n `20`; unknown avg `46.6888` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
