# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T14:52:37.953699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.2756` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.2608` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.2366` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7751` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.5972` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5567` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `-0.0711` n `239`; crypto_major avg `-0.0964` n `8`; equity avg `-0.007` n `162`; fx avg `0.0076` n `6`; index avg `-0.0077` n `27`; metal avg `-0.0119` n `20`; unknown avg `0.925` n `1262`
- 1h: commodity avg `-0.0317` n `13`; crypto_alt avg `-1.6655` n `239`; crypto_major avg `-1.6334` n `8`; equity avg `-0.3718` n `162`; fx avg `0.0026` n `6`; index avg `-0.0362` n `27`; metal avg `-0.0767` n `20`; unknown avg `159.1617` n `1258`
- 4h: commodity avg `-0.0581` n `13`; crypto_alt avg `-2.1236` n `239`; crypto_major avg `-2.3189` n `8`; equity avg `-0.5438` n `162`; fx avg `0.0236` n `6`; index avg `-0.0433` n `27`; metal avg `-0.0823` n `20`; unknown avg `0.4089` n `1248`
- 24h: commodity avg `-0.2651` n `13`; crypto_alt avg `-5.9158` n `239`; crypto_major avg `-5.8879` n `8`; equity avg `-1.7017` n `162`; fx avg `-0.1179` n `6`; index avg `-0.1501` n `27`; metal avg `-0.434` n `20`; unknown avg `1.0886` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
