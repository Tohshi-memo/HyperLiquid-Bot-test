# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T04:48:41.588027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `-0.024` n `230`; crypto_major avg `-0.0354` n `8`; equity avg `-0.175` n `120`; fx avg `-0.0106` n `6`; index avg `-0.044` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.0802` n `789`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `-0.2466` n `230`; crypto_major avg `-0.0343` n `8`; equity avg `-0.3837` n `120`; fx avg `-0.0123` n `6`; index avg `-0.0807` n `25`; metal avg `-0.0982` n `20`; unknown avg `1.184` n `789`
- 4h: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0534` n `230`; crypto_major avg `-0.1239` n `8`; equity avg `-0.2105` n `120`; fx avg `-0.1051` n `6`; index avg `-0.085` n `25`; metal avg `-0.0412` n `20`; unknown avg `0.0668` n `789`
- 24h: commodity avg `0.3015` n `12`; crypto_alt avg `0.4452` n `230`; crypto_major avg `0.2166` n `8`; equity avg `-3.5298` n `120`; fx avg `-0.183` n `6`; index avg `-0.5813` n `25`; metal avg `-0.6144` n `20`; unknown avg `-0.2309` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
