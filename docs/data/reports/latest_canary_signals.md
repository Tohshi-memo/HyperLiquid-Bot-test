# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T03:22:27.707085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `-0.1932` n `237`; crypto_major avg `-0.1118` n `8`; equity avg `-0.032` n `151`; fx avg `0.0009` n `6`; index avg `0.0013` n `26`; metal avg `-0.005` n `20`; unknown avg `-0.0519` n `1193`
- 1h: commodity avg `0.0146` n `13`; crypto_alt avg `-0.0044` n `237`; crypto_major avg `0.1811` n `8`; equity avg `-0.0186` n `151`; fx avg `-0.0115` n `6`; index avg `0.0064` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.0329` n `1191`
- 4h: commodity avg `0.0394` n `13`; crypto_alt avg `-0.0169` n `236`; crypto_major avg `0.6848` n `8`; equity avg `0.0613` n `151`; fx avg `-0.0109` n `6`; index avg `0.0157` n `26`; metal avg `0.0203` n `20`; unknown avg `0.0373` n `1185`
- 24h: commodity avg `-0.1088` n `13`; crypto_alt avg `-2.2118` n `236`; crypto_major avg `-0.4165` n `8`; equity avg `-0.9086` n `151`; fx avg `-0.0419` n `6`; index avg `-0.101` n `26`; metal avg `-0.0668` n `20`; unknown avg `3.6764` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1647`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1375`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.077`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
