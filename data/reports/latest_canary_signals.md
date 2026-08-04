# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T11:22:29.377088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1333` n `12`; crypto_alt avg `0.0204` n `230`; crypto_major avg `0.1449` n `8`; equity avg `0.1413` n `107`; fx avg `-0.0126` n `6`; index avg `0.0553` n `25`; metal avg `0.0894` n `20`; unknown avg `0.015` n `781`
- 1h: commodity avg `-0.3793` n `12`; crypto_alt avg `0.046` n `230`; crypto_major avg `0.4054` n `8`; equity avg `0.4178` n `107`; fx avg `-0.0291` n `6`; index avg `0.0878` n `25`; metal avg `0.1595` n `20`; unknown avg `0.0636` n `781`
- 4h: commodity avg `-0.2517` n `12`; crypto_alt avg `0.2651` n `230`; crypto_major avg `0.6043` n `8`; equity avg `0.7759` n `107`; fx avg `0.0015` n `6`; index avg `0.099` n `25`; metal avg `0.0873` n `20`; unknown avg `0.3302` n `781`
- 24h: commodity avg `-0.008` n `12`; crypto_alt avg `0.9374` n `230`; crypto_major avg `1.4744` n `8`; equity avg `4.8385` n `107`; fx avg `0.0826` n `6`; index avg `0.5314` n `25`; metal avg `0.4264` n `20`; unknown avg `0.8704` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
