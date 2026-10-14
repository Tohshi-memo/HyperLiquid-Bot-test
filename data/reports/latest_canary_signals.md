# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T12:22:30.799798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0449` n `13`; crypto_alt avg `-0.3776` n `235`; crypto_major avg `-0.0995` n `8`; equity avg `0.0355` n `151`; fx avg `0.0025` n `6`; index avg `0.0214` n `26`; metal avg `0.0283` n `20`; unknown avg `0.1416` n `1136`
- 1h: commodity avg `-0.081` n `13`; crypto_alt avg `-0.0215` n `235`; crypto_major avg `0.1517` n `8`; equity avg `0.1542` n `151`; fx avg `0.0153` n `6`; index avg `0.0454` n `26`; metal avg `0.0757` n `20`; unknown avg `0.1228` n `1128`
- 4h: commodity avg `-0.019` n `13`; crypto_alt avg `-0.8737` n `235`; crypto_major avg `-0.2592` n `8`; equity avg `-0.4863` n `151`; fx avg `0.0097` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0115` n `20`; unknown avg `0.5755` n `1047`
- 24h: commodity avg `0.9295` n `13`; crypto_alt avg `0.7387` n `235`; crypto_major avg `0.8867` n `8`; equity avg `0.2268` n `151`; fx avg `0.0201` n `6`; index avg `0.0738` n `26`; metal avg `-0.2729` n `20`; unknown avg `1268.7332` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1497`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1271`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0795`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0771`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0723`, n `666`, weak_sample_signal
