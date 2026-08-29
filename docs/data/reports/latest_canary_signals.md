# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T05:07:24.245159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `0.0897` n `231`; crypto_major avg `0.1166` n `8`; equity avg `0.0262` n `127`; fx avg `-0.0009` n `6`; index avg `0.0031` n `26`; metal avg `0.0213` n `20`; unknown avg `0.0673` n `793`
- 1h: commodity avg `-0.0192` n `12`; crypto_alt avg `0.3798` n `231`; crypto_major avg `0.3081` n `8`; equity avg `0.0423` n `127`; fx avg `0.0122` n `6`; index avg `0.0092` n `26`; metal avg `0.0166` n `20`; unknown avg `0.2555` n `793`
- 4h: commodity avg `-0.0413` n `12`; crypto_alt avg `0.2334` n `231`; crypto_major avg `0.4202` n `8`; equity avg `0.1293` n `127`; fx avg `0.0186` n `6`; index avg `0.0535` n `26`; metal avg `0.0377` n `20`; unknown avg `-0.122` n `793`
- 24h: commodity avg `-0.1489` n `12`; crypto_alt avg `-1.5412` n `231`; crypto_major avg `-2.0881` n `8`; equity avg `-1.7776` n `127`; fx avg `-0.0693` n `6`; index avg `-0.1646` n `26`; metal avg `-0.2231` n `20`; unknown avg `-0.3938` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
