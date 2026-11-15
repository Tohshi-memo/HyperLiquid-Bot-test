# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T00:52:30.397860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7525` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.681` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5765` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.3328` n `239`; crypto_major avg `-0.433` n `8`; equity avg `-0.0348` n `162`; fx avg `-0.0072` n `6`; index avg `-0.017` n `27`; metal avg `-0.0419` n `20`; unknown avg `-0.2095` n `1262`
- 1h: commodity avg `0.0137` n `13`; crypto_alt avg `-0.5055` n `239`; crypto_major avg `-0.5651` n `8`; equity avg `-0.1239` n `162`; fx avg `-0.0071` n `6`; index avg `-0.0284` n `27`; metal avg `-0.0867` n `20`; unknown avg `0.0157` n `1252`
- 4h: commodity avg `0.0917` n `13`; crypto_alt avg `-0.6491` n `239`; crypto_major avg `-1.7594` n `8`; equity avg `-0.0784` n `162`; fx avg `0.0094` n `6`; index avg `-0.0069` n `27`; metal avg `-0.1829` n `20`; unknown avg `0.0302` n `1198`
- 24h: commodity avg `-0.03` n `13`; crypto_alt avg `-8.5888` n `239`; crypto_major avg `-8.4605` n `8`; equity avg `-1.4448` n `162`; fx avg `0.0217` n `6`; index avg `-0.1481` n `27`; metal avg `-0.5337` n `20`; unknown avg `46.9152` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
