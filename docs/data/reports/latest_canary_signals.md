# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T13:07:55.684109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2873` n `13`; crypto_alt avg `-0.0295` n `239`; crypto_major avg `-0.0633` n `8`; equity avg `-0.225` n `163`; fx avg `0.0279` n `6`; index avg `-0.0177` n `27`; metal avg `0.0807` n `20`; unknown avg `0.3782` n `1260`
- 1h: commodity avg `0.217` n `13`; crypto_alt avg `-0.2048` n `239`; crypto_major avg `-0.153` n `8`; equity avg `-0.5639` n `163`; fx avg `0.0217` n `6`; index avg `-0.0595` n `27`; metal avg `-0.1343` n `20`; unknown avg `0.3847` n `1264`
- 4h: commodity avg `0.4823` n `13`; crypto_alt avg `-0.3867` n `239`; crypto_major avg `-0.8194` n `8`; equity avg `-1.0606` n `163`; fx avg `0.0666` n `6`; index avg `-0.1164` n `27`; metal avg `-0.0918` n `20`; unknown avg `4.151` n `1254`
- 24h: commodity avg `0.0685` n `13`; crypto_alt avg `-0.7099` n `239`; crypto_major avg `-0.6999` n `8`; equity avg `-0.8413` n `163`; fx avg `-0.1026` n `6`; index avg `-0.0879` n `27`; metal avg `-1.1828` n `20`; unknown avg `5.6634` n `1099`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
