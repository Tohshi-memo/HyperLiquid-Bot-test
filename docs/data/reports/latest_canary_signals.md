# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T03:52:29.414939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `13`; crypto_alt avg `-0.0973` n `235`; crypto_major avg `-0.0863` n `8`; equity avg `-0.0018` n `151`; fx avg `-0.005` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0098` n `20`; unknown avg `1.2176` n `1135`
- 1h: commodity avg `-0.0607` n `13`; crypto_alt avg `0.0741` n `235`; crypto_major avg `0.1758` n `8`; equity avg `-0.0971` n `151`; fx avg `0.0007` n `6`; index avg `-0.0108` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.6663` n `1133`
- 4h: commodity avg `0.0225` n `13`; crypto_alt avg `0.592` n `235`; crypto_major avg `0.7379` n `8`; equity avg `0.2863` n `151`; fx avg `-0.0079` n `6`; index avg `0.0912` n `26`; metal avg `0.1119` n `20`; unknown avg `0.8372` n `1127`
- 24h: commodity avg `0.9767` n `13`; crypto_alt avg `0.4782` n `235`; crypto_major avg `0.3733` n `8`; equity avg `0.662` n `151`; fx avg `0.0346` n `6`; index avg `0.1683` n `26`; metal avg `-0.2686` n `20`; unknown avg `0.841` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1519`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1363`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1133`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0893`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0749`, n `666`, weak_sample_signal
