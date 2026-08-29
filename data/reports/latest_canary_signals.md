# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T00:52:30.659407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.31` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `-0.1004` n `231`; crypto_major avg `-0.1243` n `8`; equity avg `-0.0045` n `127`; fx avg `-0.0001` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.1875` n `793`
- 1h: commodity avg `0.0127` n `12`; crypto_alt avg `0.015` n `231`; crypto_major avg `-0.1285` n `8`; equity avg `0.0328` n `127`; fx avg `0.0058` n `6`; index avg `-0.0077` n `26`; metal avg `0.0129` n `20`; unknown avg `0.1071` n `793`
- 4h: commodity avg `-0.0041` n `12`; crypto_alt avg `0.5105` n `231`; crypto_major avg `0.2445` n `8`; equity avg `0.0143` n `127`; fx avg `0.02` n `6`; index avg `-0.0177` n `26`; metal avg `0.0435` n `20`; unknown avg `0.3363` n `793`
- 24h: commodity avg `-0.1093` n `12`; crypto_alt avg `-3.2038` n `231`; crypto_major avg `-3.4359` n `8`; equity avg `-2.187` n `127`; fx avg `-0.1144` n `6`; index avg `-0.2595` n `26`; metal avg `-0.2303` n `20`; unknown avg `-0.5417` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
