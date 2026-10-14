# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T17:22:30.276498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0503` n `13`; crypto_alt avg `-0.1775` n `235`; crypto_major avg `-0.1955` n `8`; equity avg `-0.1212` n `151`; fx avg `0.0112` n `6`; index avg `-0.011` n `26`; metal avg `0.0059` n `20`; unknown avg `-0.0486` n `1137`
- 1h: commodity avg `0.0584` n `13`; crypto_alt avg `0.8876` n `235`; crypto_major avg `0.4695` n `8`; equity avg `0.1138` n `151`; fx avg `0.0404` n `6`; index avg `0.0074` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.2901` n `1135`
- 4h: commodity avg `0.0215` n `13`; crypto_alt avg `0.2037` n `235`; crypto_major avg `-0.4578` n `8`; equity avg `-1.6608` n `151`; fx avg `-0.0213` n `6`; index avg `-0.213` n `26`; metal avg `-0.2803` n `20`; unknown avg `-0.0591` n `1102`
- 24h: commodity avg `-0.0013` n `13`; crypto_alt avg `-2.0303` n `235`; crypto_major avg `-1.8421` n `8`; equity avg `-3.2353` n `151`; fx avg `-0.1229` n `6`; index avg `-0.4531` n `26`; metal avg `-0.8256` n `20`; unknown avg `1261.0666` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.08`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0589`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0571`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
