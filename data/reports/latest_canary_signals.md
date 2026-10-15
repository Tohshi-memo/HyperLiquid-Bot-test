# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T21:52:48.556818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `13`; crypto_alt avg `-0.1402` n `236`; crypto_major avg `-0.0497` n `8`; equity avg `0.1179` n `151`; fx avg `0.0022` n `6`; index avg `0.0175` n `26`; metal avg `-0.0045` n `20`; unknown avg `2.0652` n `1136`
- 1h: commodity avg `-0.0529` n `13`; crypto_alt avg `-0.0708` n `236`; crypto_major avg `0.0957` n `8`; equity avg `-0.1245` n `151`; fx avg `-0.0077` n `6`; index avg `-0.0193` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.7309` n `1128`
- 4h: commodity avg `-0.1976` n `13`; crypto_alt avg `0.0702` n `236`; crypto_major avg `0.0491` n `8`; equity avg `0.9972` n `151`; fx avg `-0.0193` n `6`; index avg `0.0711` n `26`; metal avg `0.0877` n `20`; unknown avg `0.0696` n `1052`
- 24h: commodity avg `-0.2916` n `13`; crypto_alt avg `0.5954` n `236`; crypto_major avg `0.6802` n `8`; equity avg `0.5559` n `151`; fx avg `0.1821` n `6`; index avg `-0.0354` n `26`; metal avg `0.5024` n `20`; unknown avg `23.7977` n `926`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0959`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0888`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0757`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0734`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0511`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0509`, n `666`, weak_sample_signal
