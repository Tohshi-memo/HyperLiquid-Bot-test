# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T01:37:28.239425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.7425` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.6769` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6405` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6212` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `-0.2255` n `239`; crypto_major avg `-0.2165` n `8`; equity avg `0.0163` n `162`; fx avg `-0.0005` n `6`; index avg `0.0071` n `27`; metal avg `0.0483` n `20`; unknown avg `0.1053` n `1262`
- 1h: commodity avg `0.0071` n `13`; crypto_alt avg `-1.0811` n `239`; crypto_major avg `-1.7601` n `8`; equity avg `-0.2737` n `162`; fx avg `0.0028` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0832` n `20`; unknown avg `0.2119` n `1260`
- 4h: commodity avg `0.1049` n `13`; crypto_alt avg `-0.3036` n `239`; crypto_major avg `-1.6375` n `8`; equity avg `-0.1751` n `162`; fx avg `0.0115` n `6`; index avg `0.003` n `27`; metal avg `-0.0163` n `20`; unknown avg `0.2685` n `1216`
- 24h: commodity avg `-0.0275` n `13`; crypto_alt avg `-9.1052` n `239`; crypto_major avg `-9.5622` n `8`; equity avg `-1.7243` n `162`; fx avg `0.025` n `6`; index avg `-0.1278` n `27`; metal avg `-0.5925` n `20`; unknown avg `46.5948` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
