# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T12:52:28.400572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.0539` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.9302` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.7193` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6322` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0365` n `12`; crypto_alt avg `0.0559` n `232`; crypto_major avg `0.2102` n `8`; equity avg `-0.0079` n `133`; fx avg `-0.1304` n `6`; index avg `-0.0144` n `26`; metal avg `0.1335` n `20`; unknown avg `0.22` n `793`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `-2.0076` n `232`; crypto_major avg `-2.0622` n `8`; equity avg `-0.9198` n `133`; fx avg `-0.1839` n `6`; index avg `-0.132` n `26`; metal avg `-0.3429` n `20`; unknown avg `2.1134` n `785`
- 4h: commodity avg `0.0183` n `12`; crypto_alt avg `-1.4884` n `232`; crypto_major avg `-1.7343` n `8`; equity avg `-0.7486` n `133`; fx avg `-0.219` n `6`; index avg `-0.1021` n `26`; metal avg `-0.4139` n `20`; unknown avg `1.1368` n `785`
- 24h: commodity avg `-0.3486` n `12`; crypto_alt avg `0.289` n `232`; crypto_major avg `1.3804` n `8`; equity avg `0.9266` n `133`; fx avg `-0.1396` n `6`; index avg `0.1892` n `26`; metal avg `-0.2086` n `20`; unknown avg `1.401` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
