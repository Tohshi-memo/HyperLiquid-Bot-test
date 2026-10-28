# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T23:52:25.128631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `-0.0392` n `238`; crypto_major avg `-0.1125` n `8`; equity avg `-0.0698` n `155`; fx avg `-0.0132` n `6`; index avg `-0.0096` n `27`; metal avg `-0.0066` n `20`; unknown avg `0.8659` n `1222`
- 1h: commodity avg `-0.05` n `13`; crypto_alt avg `-0.1573` n `238`; crypto_major avg `-0.1085` n `8`; equity avg `-0.1153` n `155`; fx avg `-0.0173` n `6`; index avg `-0.0104` n `27`; metal avg `0.0222` n `20`; unknown avg `0.2877` n `1176`
- 4h: commodity avg `-0.2275` n `13`; crypto_alt avg `-0.4079` n `238`; crypto_major avg `-0.2532` n `8`; equity avg `-1.2646` n `155`; fx avg `-0.0344` n `6`; index avg `-0.1985` n `27`; metal avg `-0.0613` n `20`; unknown avg `4.0076` n `1048`
- 24h: commodity avg `0.1106` n `13`; crypto_alt avg `0.3331` n `238`; crypto_major avg `0.3687` n `8`; equity avg `0.3867` n `154`; fx avg `0.2138` n `6`; index avg `0.0817` n `27`; metal avg `-0.169` n `20`; unknown avg `26.2434` n `994`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
