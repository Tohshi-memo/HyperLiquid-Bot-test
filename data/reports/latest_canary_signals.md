# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T15:22:24.033417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.4648` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.4551` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.3954` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9523` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.5847` n `239`; crypto_major avg `-0.5091` n `8`; equity avg `-0.1384` n `162`; fx avg `-0.0073` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0312` n `20`; unknown avg `0.3108` n `1260`
- 1h: commodity avg `-0.0349` n `13`; crypto_alt avg `-0.5318` n `239`; crypto_major avg `-0.5994` n `8`; equity avg `-0.1354` n `162`; fx avg `-0.0021` n `6`; index avg `-0.0187` n `27`; metal avg `-0.0602` n `20`; unknown avg `0.8659` n `1254`
- 4h: commodity avg `-0.05` n `13`; crypto_alt avg `-2.6161` n `239`; crypto_major avg `-2.5051` n `8`; equity avg `-0.5528` n `162`; fx avg `0.0173` n `6`; index avg `-0.0403` n `27`; metal avg `-0.1097` n `20`; unknown avg `-0.1263` n `1252`
- 24h: commodity avg `-0.184` n `13`; crypto_alt avg `-5.4824` n `239`; crypto_major avg `-5.1334` n `8`; equity avg `-0.1539` n `162`; fx avg `-0.1246` n `6`; index avg `-0.0004` n `27`; metal avg `-0.3098` n `20`; unknown avg `1.3` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
