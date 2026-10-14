# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T09:52:29.129483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `13`; crypto_alt avg `0.0732` n `235`; crypto_major avg `0.0079` n `8`; equity avg `0.0801` n `151`; fx avg `-0.0067` n `6`; index avg `0.0128` n `26`; metal avg `0.0615` n `20`; unknown avg `0.0454` n `1135`
- 1h: commodity avg `0.0395` n `13`; crypto_alt avg `-0.5808` n `235`; crypto_major avg `-0.2972` n `8`; equity avg `-0.0433` n `151`; fx avg `0.0013` n `6`; index avg `0.0134` n `26`; metal avg `0.028` n `20`; unknown avg `0.0754` n `1101`
- 4h: commodity avg `0.0193` n `13`; crypto_alt avg `-0.4907` n `235`; crypto_major avg `-0.2124` n `8`; equity avg `-0.0581` n `151`; fx avg `-0.0482` n `6`; index avg `0.0282` n `26`; metal avg `-0.0955` n `20`; unknown avg `1149.3099` n `1021`
- 24h: commodity avg `1.1546` n `13`; crypto_alt avg `-0.7136` n `235`; crypto_major avg `-0.3355` n `8`; equity avg `-0.4344` n `151`; fx avg `0.0491` n `6`; index avg `-0.0072` n `26`; metal avg `-0.4627` n `20`; unknown avg `1203.0839` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1522`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1314`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0739`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.073`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0723`, n `666`, weak_sample_signal
