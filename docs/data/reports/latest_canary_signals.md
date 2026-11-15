# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T17:37:26.779688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7282` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7177` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5933` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0026` n `13`; crypto_alt avg `-0.3154` n `239`; crypto_major avg `-0.4571` n `8`; equity avg `-0.1009` n `162`; fx avg `0.0` n `6`; index avg `-0.0026` n `27`; metal avg `0.0071` n `20`; unknown avg `1.1061` n `1265`
- 1h: commodity avg `-0.027` n `13`; crypto_alt avg `-0.5246` n `239`; crypto_major avg `-0.3431` n `8`; equity avg `-0.1707` n `162`; fx avg `0.0077` n `6`; index avg `-0.0318` n `27`; metal avg `-0.0017` n `20`; unknown avg `3.5676` n `1263`
- 4h: commodity avg `-0.0157` n `13`; crypto_alt avg `-1.7` n `239`; crypto_major avg `-1.7246` n `8`; equity avg `-0.1313` n `162`; fx avg `0.0072` n `6`; index avg `0.0036` n `27`; metal avg `-0.0069` n `20`; unknown avg `160.6027` n `1256`
- 24h: commodity avg `0.0408` n `13`; crypto_alt avg `-2.3516` n `239`; crypto_major avg `-1.6716` n `8`; equity avg `-0.0428` n `162`; fx avg `-0.0125` n `6`; index avg `0.0107` n `27`; metal avg `-0.1697` n `20`; unknown avg `0.358` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
