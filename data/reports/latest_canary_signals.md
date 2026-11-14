# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T15:37:35.411488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2623` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2494` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1723` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6513` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0` n `13`; crypto_alt avg `0.0897` n `239`; crypto_major avg `-0.0029` n `8`; equity avg `-0.131` n `162`; fx avg `0.0002` n `6`; index avg `-0.0151` n `27`; metal avg `-0.0244` n `20`; unknown avg `158.8067` n `1262`
- 1h: commodity avg `-0.0043` n `13`; crypto_alt avg `-0.3609` n `239`; crypto_major avg `-0.2966` n `8`; equity avg `-0.1588` n `162`; fx avg `-0.0032` n `6`; index avg `-0.0203` n `27`; metal avg `-0.0724` n `20`; unknown avg `0.5865` n `1258`
- 4h: commodity avg `-0.0412` n `13`; crypto_alt avg `-2.4357` n `239`; crypto_major avg `-2.3035` n `8`; equity avg `-0.6522` n `162`; fx avg `0.0065` n `6`; index avg `-0.0541` n `27`; metal avg `-0.1312` n `20`; unknown avg `0.1993` n `1250`
- 24h: commodity avg `-0.1378` n `13`; crypto_alt avg `-4.974` n `239`; crypto_major avg `-4.5924` n `8`; equity avg `-0.1475` n `162`; fx avg `-0.1168` n `6`; index avg `0.0015` n `27`; metal avg `-0.3117` n `20`; unknown avg `1.6143` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
