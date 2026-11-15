# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T17:27:44.840852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5533` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5203` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.512` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0038` n `13`; crypto_alt avg `-0.0224` n `239`; crypto_major avg `0.0699` n `8`; equity avg `-0.0468` n `162`; fx avg `0.007` n `6`; index avg `-0.014` n `27`; metal avg `-0.0106` n `20`; unknown avg `0.6755` n `1261`
- 1h: commodity avg `0.0022` n `13`; crypto_alt avg `-0.1805` n `239`; crypto_major avg `0.2311` n `8`; equity avg `0.1396` n `162`; fx avg `0.0046` n `6`; index avg `-0.0162` n `27`; metal avg `0.0007` n `20`; unknown avg `161.2509` n `1261`
- 4h: commodity avg `-0.0796` n `13`; crypto_alt avg `-1.5414` n `239`; crypto_major avg `-1.5481` n `8`; equity avg `-0.0361` n `162`; fx avg `0.01` n `6`; index avg `0.0052` n `27`; metal avg `-0.0278` n `20`; unknown avg `1.2248` n `1254`
- 24h: commodity avg `0.0439` n `13`; crypto_alt avg `-1.2822` n `239`; crypto_major avg `-0.2287` n `8`; equity avg `0.2122` n `162`; fx avg `-0.0085` n `6`; index avg `0.031` n `27`; metal avg `-0.1668` n `20`; unknown avg `0.6968` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
