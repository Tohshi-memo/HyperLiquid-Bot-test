# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T19:52:33.330559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1465` n `13`; crypto_alt avg `0.0186` n `236`; crypto_major avg `0.1011` n `8`; equity avg `-0.0648` n `151`; fx avg `0.007` n `6`; index avg `-0.0014` n `26`; metal avg `0.0134` n `20`; unknown avg `29.1648` n `1128`
- 1h: commodity avg `0.1296` n `13`; crypto_alt avg `-0.1049` n `236`; crypto_major avg `0.1717` n `8`; equity avg `0.0775` n `151`; fx avg `0.0296` n `6`; index avg `0.0191` n `26`; metal avg `0.0142` n `20`; unknown avg `8.056` n `1118`
- 4h: commodity avg `0.1919` n `13`; crypto_alt avg `0.4725` n `236`; crypto_major avg `0.2044` n `8`; equity avg `-0.771` n `151`; fx avg `0.0209` n `6`; index avg `-0.1209` n `26`; metal avg `-0.0361` n `20`; unknown avg `6.9779` n `1108`
- 24h: commodity avg `-0.0381` n `13`; crypto_alt avg `-2.5703` n `236`; crypto_major avg `-1.8764` n `8`; equity avg `-3.844` n `151`; fx avg `-0.1439` n `6`; index avg `-0.5307` n `26`; metal avg `-0.8625` n `20`; unknown avg `1293.1435` n `960`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0956`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0826`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0609`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0574`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
