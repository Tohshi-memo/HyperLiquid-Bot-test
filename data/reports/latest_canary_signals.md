# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T13:22:28.364940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `0.0025` n `232`; crypto_major avg `0.0942` n `8`; equity avg `0.0039` n `133`; fx avg `0.0076` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0415` n `20`; unknown avg `0.0704` n `792`
- 1h: commodity avg `-0.0846` n `12`; crypto_alt avg `0.1839` n `232`; crypto_major avg `0.6309` n `8`; equity avg `0.5411` n `133`; fx avg `0.0234` n `6`; index avg `0.1127` n `26`; metal avg `0.275` n `20`; unknown avg `13.9738` n `790`
- 4h: commodity avg `0.0486` n `12`; crypto_alt avg `0.3174` n `232`; crypto_major avg `0.904` n `8`; equity avg `0.3785` n `133`; fx avg `-0.0766` n `6`; index avg `0.0585` n `26`; metal avg `0.2355` n `20`; unknown avg `2.3035` n `790`
- 24h: commodity avg `0.4519` n `12`; crypto_alt avg `2.4459` n `232`; crypto_major avg `2.6993` n `8`; equity avg `1.4566` n `133`; fx avg `-0.3979` n `6`; index avg `0.149` n `26`; metal avg `0.7555` n `20`; unknown avg `0.1829` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0416`, n `668`, weak_sample_signal
