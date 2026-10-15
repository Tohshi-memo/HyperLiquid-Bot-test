# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T07:52:30.396477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0303` n `13`; crypto_alt avg `0.1178` n `236`; crypto_major avg `0.1198` n `8`; equity avg `0.053` n `151`; fx avg `-0.0275` n `6`; index avg `0.0149` n `26`; metal avg `-0.0018` n `20`; unknown avg `8.7376` n `1136`
- 1h: commodity avg `-0.0644` n `13`; crypto_alt avg `0.1165` n `236`; crypto_major avg `0.4712` n `8`; equity avg `0.0309` n `151`; fx avg `0.0069` n `6`; index avg `0.0555` n `26`; metal avg `0.1298` n `20`; unknown avg `8.9256` n `1134`
- 4h: commodity avg `-0.0284` n `13`; crypto_alt avg `0.1173` n `236`; crypto_major avg `0.6471` n `8`; equity avg `-0.0435` n `151`; fx avg `-0.0668` n `6`; index avg `0.0905` n `26`; metal avg `0.094` n `20`; unknown avg `7.8638` n `1102`
- 24h: commodity avg `-0.3889` n `13`; crypto_alt avg `-5.2551` n `236`; crypto_major avg `-3.3803` n `8`; equity avg `-5.8301` n `151`; fx avg `0.0499` n `6`; index avg `-0.9217` n `26`; metal avg `-0.5373` n `20`; unknown avg `1392.7309` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1146`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1007`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0904`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0856`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0838`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0786`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0709`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
