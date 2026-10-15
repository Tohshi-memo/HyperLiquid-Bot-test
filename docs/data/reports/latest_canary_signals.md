# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T11:22:39.018311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `13`; crypto_alt avg `0.1614` n `236`; crypto_major avg `0.0489` n `8`; equity avg `0.3457` n `151`; fx avg `0.0061` n `6`; index avg `0.0431` n `26`; metal avg `0.0172` n `20`; unknown avg `0.1379` n `1136`
- 1h: commodity avg `0.06` n `13`; crypto_alt avg `0.1019` n `236`; crypto_major avg `0.0485` n `8`; equity avg `-0.2907` n `151`; fx avg `0.0372` n `6`; index avg `-0.0231` n `26`; metal avg `0.0154` n `20`; unknown avg `-0.3459` n `1110`
- 4h: commodity avg `0.0944` n `13`; crypto_alt avg `0.1232` n `236`; crypto_major avg `-0.0637` n `8`; equity avg `-0.3728` n `151`; fx avg `0.0267` n `6`; index avg `-0.0` n `26`; metal avg `0.1524` n `20`; unknown avg `4.1741` n `1038`
- 24h: commodity avg `-0.3725` n `13`; crypto_alt avg `-4.7787` n `236`; crypto_major avg `-3.6287` n `8`; equity avg `-5.9677` n `151`; fx avg `0.0708` n `6`; index avg `-0.9544` n `26`; metal avg `-0.3939` n `20`; unknown avg `1.8972` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1182`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.088`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0835`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0717`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.068`, n `666`, weak_sample_signal
