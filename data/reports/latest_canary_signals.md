# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T15:37:36.968446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4576` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0237` n `13`; crypto_alt avg `0.0048` n `235`; crypto_major avg `-0.1515` n `8`; equity avg `-0.3808` n `151`; fx avg `-0.0081` n `6`; index avg `-0.0548` n `26`; metal avg `-0.0496` n `20`; unknown avg `1.3641` n `1137`
- 1h: commodity avg `-0.0454` n `13`; crypto_alt avg `0.3384` n `235`; crypto_major avg `0.4279` n `8`; equity avg `-0.657` n `151`; fx avg `-0.0269` n `6`; index avg `-0.1078` n `26`; metal avg `-0.145` n `20`; unknown avg `1.322` n `1110`
- 4h: commodity avg `-0.291` n `13`; crypto_alt avg `-2.0347` n `235`; crypto_major avg `-1.8066` n `8`; equity avg `-2.4576` n `151`; fx avg `-0.1321` n `6`; index avg `-0.349` n `26`; metal avg `-0.6702` n `20`; unknown avg `3.8699` n `1102`
- 24h: commodity avg `-0.0207` n `13`; crypto_alt avg `-2.0972` n `235`; crypto_major avg `-1.591` n `8`; equity avg `-2.3495` n `151`; fx avg `-0.1634` n `6`; index avg `-0.2898` n `26`; metal avg `-0.8039` n `20`; unknown avg `1262.4025` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0808`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0732`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0715`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0655`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0654`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
