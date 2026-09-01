# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T12:07:28.364411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `-0.203` n `232`; crypto_major avg `-0.1703` n `8`; equity avg `-0.2344` n `130`; fx avg `0.0042` n `6`; index avg `-0.0449` n `26`; metal avg `-0.0788` n `20`; unknown avg `-0.005` n `790`
- 1h: commodity avg `-0.0744` n `12`; crypto_alt avg `0.3546` n `232`; crypto_major avg `0.227` n `8`; equity avg `-0.1774` n `130`; fx avg `0.0025` n `6`; index avg `-0.0298` n `26`; metal avg `-0.0214` n `20`; unknown avg `-0.0699` n `790`
- 4h: commodity avg `-0.1076` n `12`; crypto_alt avg `-0.0633` n `232`; crypto_major avg `-0.0605` n `8`; equity avg `-0.9988` n `130`; fx avg `0.0264` n `6`; index avg `-0.2139` n `26`; metal avg `-0.3973` n `20`; unknown avg `-0.4192` n `790`
- 24h: commodity avg `0.2377` n `12`; crypto_alt avg `0.8461` n `232`; crypto_major avg `0.1244` n `8`; equity avg `-0.9151` n `130`; fx avg `0.1111` n `6`; index avg `-0.3067` n `26`; metal avg `-0.8662` n `20`; unknown avg `-0.052` n `750`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0348`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0294`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0281`, n `668`, weak_sample_signal
