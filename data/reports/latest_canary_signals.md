# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T13:22:35.005321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1074` n `13`; crypto_alt avg `0.1967` n `239`; crypto_major avg `-0.0079` n `8`; equity avg `0.0853` n `163`; fx avg `-0.008` n `6`; index avg `0.0099` n `27`; metal avg `0.0286` n `20`; unknown avg `2.0439` n `1264`
- 1h: commodity avg `0.0935` n `13`; crypto_alt avg `-0.1161` n `239`; crypto_major avg `-0.4276` n `8`; equity avg `-0.6108` n `163`; fx avg `0.0156` n `6`; index avg `-0.069` n `27`; metal avg `-0.1071` n `20`; unknown avg `0.4064` n `1264`
- 4h: commodity avg `0.4018` n `13`; crypto_alt avg `-0.1613` n `239`; crypto_major avg `-0.6857` n `8`; equity avg `-0.8925` n `163`; fx avg `0.0468` n `6`; index avg `-0.1118` n `27`; metal avg `-0.0044` n `20`; unknown avg `4.9418` n `1256`
- 24h: commodity avg `-0.0873` n `13`; crypto_alt avg `-0.4311` n `239`; crypto_major avg `-0.5879` n `8`; equity avg `-0.4717` n `163`; fx avg `-0.0996` n `6`; index avg `-0.0399` n `27`; metal avg `-1.0428` n `20`; unknown avg `2.7737` n `1137`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
