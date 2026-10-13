# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T13:37:28.868602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `0.2698` n `235`; crypto_major avg `0.284` n `8`; equity avg `0.1434` n `151`; fx avg `0.0039` n `6`; index avg `0.0472` n `26`; metal avg `0.0335` n `20`; unknown avg `7.4605` n `1131`
- 1h: commodity avg `0.2584` n `13`; crypto_alt avg `0.6391` n `235`; crypto_major avg `0.3322` n `8`; equity avg `-0.0242` n `151`; fx avg `0.033` n `6`; index avg `0.0228` n `26`; metal avg `-0.0156` n `20`; unknown avg `6.6289` n `1125`
- 4h: commodity avg `0.3903` n `13`; crypto_alt avg `-0.1522` n `235`; crypto_major avg `-0.0165` n `8`; equity avg `-0.9071` n `151`; fx avg `0.0681` n `6`; index avg `-0.0619` n `26`; metal avg `-0.1186` n `20`; unknown avg `2.621` n `1119`
- 24h: commodity avg `0.0972` n `13`; crypto_alt avg `-2.7724` n `235`; crypto_major avg `-1.0938` n `8`; equity avg `-2.557` n `151`; fx avg `0.1055` n `6`; index avg `-0.2976` n `26`; metal avg `-0.046` n `20`; unknown avg `1.8094` n `986`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1697`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1589`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1511`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1345`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0877`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
