# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T17:07:25.818946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `13`; crypto_alt avg `0.0421` n `235`; crypto_major avg `0.0612` n `8`; equity avg `-0.0186` n `151`; fx avg `0.0054` n `6`; index avg `-0.0164` n `26`; metal avg `0.0018` n `20`; unknown avg `-0.0265` n `1135`
- 1h: commodity avg `0.0747` n `13`; crypto_alt avg `0.8383` n `235`; crypto_major avg `0.359` n `8`; equity avg `-0.1604` n `151`; fx avg `-0.0001` n `6`; index avg `-0.0467` n `26`; metal avg `-0.0108` n `20`; unknown avg `0.4533` n `1135`
- 4h: commodity avg `0.0616` n `13`; crypto_alt avg `-0.1996` n `235`; crypto_major avg `-0.7396` n `8`; equity avg `-1.6542` n `151`; fx avg `-0.0259` n `6`; index avg `-0.2092` n `26`; metal avg `-0.3329` n `20`; unknown avg `0.0661` n `1102`
- 24h: commodity avg `0.069` n `13`; crypto_alt avg `-1.7869` n `235`; crypto_major avg `-1.5924` n `8`; equity avg `-3.1778` n `151`; fx avg `-0.1278` n `6`; index avg `-0.4522` n `26`; metal avg `-0.8148` n `20`; unknown avg `1261.1406` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0679`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0579`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
