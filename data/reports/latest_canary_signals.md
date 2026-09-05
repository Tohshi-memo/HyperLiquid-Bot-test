# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T17:07:26.977330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `0.3912` n `232`; crypto_major avg `0.2697` n `8`; equity avg `0.027` n `134`; fx avg `-0.0002` n `6`; index avg `-0.0025` n `26`; metal avg `0.0041` n `20`; unknown avg `0.2375` n `792`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `0.5186` n `232`; crypto_major avg `0.611` n `8`; equity avg `0.0373` n `134`; fx avg `0.0247` n `6`; index avg `0.0174` n `26`; metal avg `0.0194` n `20`; unknown avg `0.0484` n `786`
- 4h: commodity avg `0.0701` n `12`; crypto_alt avg `0.2136` n `232`; crypto_major avg `0.7262` n `8`; equity avg `0.0725` n `134`; fx avg `0.0122` n `6`; index avg `0.0065` n `26`; metal avg `0.0355` n `20`; unknown avg `-0.2806` n `730`
- 24h: commodity avg `0.0879` n `12`; crypto_alt avg `2.5481` n `232`; crypto_major avg `2.3153` n `8`; equity avg `0.2978` n `134`; fx avg `0.0063` n `6`; index avg `0.0212` n `26`; metal avg `0.0726` n `20`; unknown avg `0.2071` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
