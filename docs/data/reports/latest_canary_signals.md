# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T09:37:31.464556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0669` n `12`; crypto_alt avg `0.1038` n `230`; crypto_major avg `0.2069` n `8`; equity avg `0.011` n `112`; fx avg `-0.0104` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.043` n `782`
- 1h: commodity avg `-0.152` n `12`; crypto_alt avg `0.0621` n `230`; crypto_major avg `0.5838` n `8`; equity avg `0.0885` n `112`; fx avg `-0.0058` n `6`; index avg `0.0293` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0145` n `782`
- 4h: commodity avg `-0.2293` n `12`; crypto_alt avg `0.3694` n `230`; crypto_major avg `1.1811` n `8`; equity avg `0.8435` n `112`; fx avg `-0.0424` n `6`; index avg `0.1116` n `25`; metal avg `0.3742` n `20`; unknown avg `0.0911` n `766`
- 24h: commodity avg `0.4029` n `12`; crypto_alt avg `0.5604` n `230`; crypto_major avg `0.1229` n `8`; equity avg `2.1077` n `109`; fx avg `-0.0914` n `6`; index avg `0.0685` n `25`; metal avg `0.2722` n `20`; unknown avg `110.9257` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
