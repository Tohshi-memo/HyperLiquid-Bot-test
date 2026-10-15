# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T07:07:30.090704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0069` n `13`; crypto_alt avg `-0.3263` n `236`; crypto_major avg `-0.055` n `8`; equity avg `-0.0711` n `151`; fx avg `-0.0226` n `6`; index avg `-0.0024` n `26`; metal avg `0.0797` n `20`; unknown avg `1.4641` n `1134`
- 1h: commodity avg `0.0271` n `13`; crypto_alt avg `0.0713` n `236`; crypto_major avg `0.1387` n `8`; equity avg `-0.3729` n `151`; fx avg `-0.09` n `6`; index avg `-0.0096` n `26`; metal avg `0.0713` n `20`; unknown avg `1.5687` n `1128`
- 4h: commodity avg `-0.0042` n `13`; crypto_alt avg `-0.9831` n `236`; crypto_major avg `-0.338` n `8`; equity avg `-0.4318` n `151`; fx avg `-0.1505` n `6`; index avg `0.0017` n `26`; metal avg `-0.0519` n `20`; unknown avg `2.4523` n `1102`
- 24h: commodity avg `-0.4017` n `13`; crypto_alt avg `-5.8302` n `236`; crypto_major avg `-4.0159` n `8`; equity avg `-6.0437` n `151`; fx avg `0.01` n `6`; index avg `-0.9975` n `26`; metal avg `-0.6073` n `20`; unknown avg `1394.999` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.114`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0905`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0891`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0855`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.063`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
