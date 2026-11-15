# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T07:52:25.554808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8804` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8624` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0209` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0153` n `13`; crypto_alt avg `-0.3373` n `239`; crypto_major avg `-0.4309` n `8`; equity avg `-0.0791` n `162`; fx avg `-0.0017` n `6`; index avg `0.0237` n `27`; metal avg `-0.0074` n `20`; unknown avg `0.6738` n `1263`
- 1h: commodity avg `-0.0421` n `13`; crypto_alt avg `-0.9077` n `239`; crypto_major avg `-1.0046` n `8`; equity avg `-0.1591` n `162`; fx avg `-0.007` n `6`; index avg `0.0163` n `27`; metal avg `0.0466` n `20`; unknown avg `0.3715` n `1261`
- 4h: commodity avg `0.0102` n `13`; crypto_alt avg `-1.0568` n `239`; crypto_major avg `-1.8636` n `8`; equity avg `-0.391` n `162`; fx avg `-0.0012` n `6`; index avg `-0.0012` n `27`; metal avg `0.0168` n `20`; unknown avg `0.9241` n `1227`
- 24h: commodity avg `-0.0123` n `13`; crypto_alt avg `-5.5457` n `239`; crypto_major avg `-5.3338` n `8`; equity avg `-1.0971` n `162`; fx avg `0.0456` n `6`; index avg `-0.074` n `27`; metal avg `-0.426` n `20`; unknown avg `47.0913` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
