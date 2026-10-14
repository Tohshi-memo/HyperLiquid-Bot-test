# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T00:07:29.909789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `13`; crypto_alt avg `0.0732` n `235`; crypto_major avg `0.0735` n `8`; equity avg `0.0913` n `151`; fx avg `-0.0081` n `6`; index avg `0.0309` n `26`; metal avg `0.0327` n `20`; unknown avg `3.5737` n `1127`
- 1h: commodity avg `-0.0069` n `13`; crypto_alt avg `0.2705` n `235`; crypto_major avg `0.0653` n `8`; equity avg `-0.0263` n `151`; fx avg `-0.0248` n `6`; index avg `-0.0041` n `26`; metal avg `0.003` n `20`; unknown avg `3.2928` n `1127`
- 4h: commodity avg `-0.0411` n `13`; crypto_alt avg `-0.1452` n `235`; crypto_major avg `-0.219` n `8`; equity avg `-0.0189` n `151`; fx avg `-0.0073` n `6`; index avg `-0.0235` n `26`; metal avg `-0.022` n `20`; unknown avg `4.8071` n `1027`
- 24h: commodity avg `0.8197` n `13`; crypto_alt avg `1.9153` n `235`; crypto_major avg `2.1255` n `8`; equity avg `0.5704` n `151`; fx avg `0.126` n `6`; index avg `-0.0083` n `26`; metal avg `-0.2088` n `20`; unknown avg `3.9005` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1574`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1435`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0935`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0799`, n `666`, weak_sample_signal
