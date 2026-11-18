# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T16:37:28.403056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.8887` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8477` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.1318` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0572` n `13`; crypto_alt avg `0.1401` n `239`; crypto_major avg `0.0262` n `8`; equity avg `0.0371` n `164`; fx avg `0.0058` n `6`; index avg `0.0222` n `27`; metal avg `-0.0297` n `20`; unknown avg `0.0566` n `1265`
- 1h: commodity avg `-0.0435` n `13`; crypto_alt avg `-0.8839` n `239`; crypto_major avg `-1.1719` n `8`; equity avg `-0.4063` n `164`; fx avg `-0.021` n `6`; index avg `-0.0401` n `27`; metal avg `-0.1184` n `20`; unknown avg `-0.5779` n `1257`
- 4h: commodity avg `-0.2833` n `13`; crypto_alt avg `-1.4844` n `239`; crypto_major avg `-2.0492` n `8`; equity avg `-1.8951` n `164`; fx avg `-0.0387` n `6`; index avg `-0.1605` n `27`; metal avg `-0.2015` n `20`; unknown avg `1.9829` n `1257`
- 24h: commodity avg `-0.3352` n `13`; crypto_alt avg `-0.3926` n `239`; crypto_major avg `-0.7799` n `8`; equity avg `0.1798` n `164`; fx avg `-0.1929` n `6`; index avg `0.0317` n `27`; metal avg `-1.2644` n `20`; unknown avg `0.0961` n `1138`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
