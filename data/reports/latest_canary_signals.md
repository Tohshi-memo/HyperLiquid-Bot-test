# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T15:37:31.577059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0678` n `13`; crypto_alt avg `-0.5756` n `235`; crypto_major avg `-0.5067` n `8`; equity avg `-0.2575` n `151`; fx avg `-0.0122` n `6`; index avg `-0.0346` n `26`; metal avg `-0.0459` n `20`; unknown avg `0.5104` n `1135`
- 1h: commodity avg `0.0879` n `13`; crypto_alt avg `-0.517` n `235`; crypto_major avg `-0.4372` n `8`; equity avg `-0.4429` n `151`; fx avg `0.0025` n `6`; index avg `-0.0883` n `26`; metal avg `-0.0398` n `20`; unknown avg `1.437` n `1129`
- 4h: commodity avg `0.7786` n `13`; crypto_alt avg `0.3705` n `235`; crypto_major avg `0.0145` n `8`; equity avg `-0.374` n `151`; fx avg `0.0483` n `6`; index avg `-0.0454` n `26`; metal avg `-0.3331` n `20`; unknown avg `1.6215` n `1091`
- 24h: commodity avg `0.3208` n `13`; crypto_alt avg `-2.5142` n `235`; crypto_major avg `-1.1065` n `8`; equity avg `-1.7725` n `151`; fx avg `0.1343` n `6`; index avg `-0.3122` n `26`; metal avg `-0.2117` n `20`; unknown avg `0.7539` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1643`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1488`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1374`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0915`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
