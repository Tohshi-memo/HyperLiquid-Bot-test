# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T14:37:37.372025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2565` n `13`; crypto_alt avg `-0.3839` n `235`; crypto_major avg `-0.1629` n `8`; equity avg `0.0671` n `150`; fx avg `0.0279` n `6`; index avg `0.0102` n `26`; metal avg `-0.0173` n `20`; unknown avg `-0.145` n `1053`
- 1h: commodity avg `-0.111` n `13`; crypto_alt avg `0.6912` n `235`; crypto_major avg `0.3908` n `8`; equity avg `0.2492` n `150`; fx avg `0.0528` n `6`; index avg `0.0533` n `26`; metal avg `0.0452` n `20`; unknown avg `0.4817` n `1027`
- 4h: commodity avg `-0.1957` n `13`; crypto_alt avg `-0.1917` n `235`; crypto_major avg `-0.6943` n `8`; equity avg `0.2584` n `150`; fx avg `0.0489` n `6`; index avg `0.1419` n `26`; metal avg `0.0772` n `20`; unknown avg `1.3791` n `1021`
- 24h: commodity avg `0.6014` n `13`; crypto_alt avg `1.1977` n `235`; crypto_major avg `-1.5202` n `8`; equity avg `-1.061` n `150`; fx avg `0.1039` n `6`; index avg `-0.0571` n `26`; metal avg `0.0242` n `20`; unknown avg `22.3529` n `990`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
