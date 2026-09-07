# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T09:22:25.838662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.3322` n `232`; crypto_major avg `0.2256` n `8`; equity avg `-0.029` n `134`; fx avg `0.025` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0117` n `20`; unknown avg `-0.0843` n `792`
- 1h: commodity avg `0.0769` n `12`; crypto_alt avg `0.5505` n `232`; crypto_major avg `0.2972` n `8`; equity avg `-0.0038` n `134`; fx avg `0.0175` n `6`; index avg `-0.008` n `26`; metal avg `-0.0918` n `20`; unknown avg `1.2782` n `784`
- 4h: commodity avg `-0.1461` n `12`; crypto_alt avg `0.0816` n `232`; crypto_major avg `-0.2372` n `8`; equity avg `0.0505` n `134`; fx avg `-0.1389` n `6`; index avg `0.0436` n `26`; metal avg `0.1049` n `20`; unknown avg `2.0011` n `758`
- 24h: commodity avg `-0.0895` n `12`; crypto_alt avg `0.4435` n `232`; crypto_major avg `-0.66` n `8`; equity avg `0.4034` n `134`; fx avg `-0.1166` n `6`; index avg `0.0403` n `26`; metal avg `-0.0972` n `20`; unknown avg `76.8471` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
