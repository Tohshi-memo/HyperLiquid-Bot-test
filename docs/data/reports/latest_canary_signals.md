# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T06:52:38.601790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0314` n `12`; crypto_alt avg `-0.0929` n `232`; crypto_major avg `0.0156` n `8`; equity avg `0.0451` n `134`; fx avg `-0.01` n `6`; index avg `0.0074` n `26`; metal avg `0.0369` n `20`; unknown avg `0.8375` n `796`
- 1h: commodity avg `-0.0723` n `12`; crypto_alt avg `-0.1821` n `232`; crypto_major avg `-0.2011` n `8`; equity avg `0.0651` n `134`; fx avg `-0.0383` n `6`; index avg `0.0386` n `26`; metal avg `0.0448` n `20`; unknown avg `0.2454` n `764`
- 4h: commodity avg `0.1154` n `12`; crypto_alt avg `-0.7458` n `232`; crypto_major avg `-0.7856` n `8`; equity avg `0.1169` n `134`; fx avg `-0.0744` n `6`; index avg `0.0524` n `26`; metal avg `-0.0448` n `20`; unknown avg `0.218` n `758`
- 24h: commodity avg `0.0669` n `12`; crypto_alt avg `0.0994` n `232`; crypto_major avg `-0.5814` n `8`; equity avg `0.4521` n `134`; fx avg `-0.0385` n `6`; index avg `0.0555` n `26`; metal avg `-0.1308` n `20`; unknown avg `382.8304` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
