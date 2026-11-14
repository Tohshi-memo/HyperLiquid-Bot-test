# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T16:37:24.601651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.3059` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.2735` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.158` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.3946` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0134` n `13`; crypto_alt avg `-0.1732` n `239`; crypto_major avg `-0.1608` n `8`; equity avg `-0.1207` n `162`; fx avg `0.0022` n `6`; index avg `-0.0143` n `27`; metal avg `0.0303` n `20`; unknown avg `0.414` n `1262`
- 1h: commodity avg `-0.0213` n `13`; crypto_alt avg `-1.2089` n `239`; crypto_major avg `-0.9846` n `8`; equity avg `-0.3356` n `162`; fx avg `0.0054` n `6`; index avg `-0.0415` n `27`; metal avg `-0.0798` n `20`; unknown avg `0.1446` n `1254`
- 4h: commodity avg `-0.0663` n `13`; crypto_alt avg `-3.6703` n `239`; crypto_major avg `-3.3722` n `8`; equity avg `-0.9776` n `162`; fx avg `0.0072` n `6`; index avg `-0.0987` n `27`; metal avg `-0.2142` n `20`; unknown avg `160.1593` n `1250`
- 24h: commodity avg `-0.0449` n `13`; crypto_alt avg `-6.799` n `239`; crypto_major avg `-5.9645` n `8`; equity avg `-1.0074` n `162`; fx avg `-0.075` n `6`; index avg `-0.0657` n `27`; metal avg `-0.3571` n `20`; unknown avg `1.7757` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
