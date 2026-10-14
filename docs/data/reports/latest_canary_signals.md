# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T16:52:32.592200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0726` n `13`; crypto_alt avg `0.4836` n `235`; crypto_major avg `0.2653` n `8`; equity avg `0.1236` n `151`; fx avg `0.0119` n `6`; index avg `0.0226` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.0975` n `1137`
- 1h: commodity avg `0.1474` n `13`; crypto_alt avg `0.9367` n `235`; crypto_major avg `0.3937` n `8`; equity avg `-0.2126` n `151`; fx avg `-0.0002` n `6`; index avg `-0.0427` n `26`; metal avg `-0.0321` n `20`; unknown avg `0.9816` n `1129`
- 4h: commodity avg `0.0561` n `13`; crypto_alt avg `-0.6549` n `235`; crypto_major avg `-1.0775` n `8`; equity avg `-1.9013` n `151`; fx avg `-0.0524` n `6`; index avg `-0.249` n `26`; metal avg `-0.523` n `20`; unknown avg `0.9974` n `1102`
- 24h: commodity avg `0.0833` n `13`; crypto_alt avg `-2.145` n `235`; crypto_major avg `-1.911` n `8`; equity avg `-3.3663` n `151`; fx avg `-0.1372` n `6`; index avg `-0.4512` n `26`; metal avg `-0.8201` n `20`; unknown avg `1261.8375` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0805`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0673`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.057`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
