# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T03:37:25.718713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.4356` n `234`; crypto_major avg `0.2582` n `8`; equity avg `0.1718` n `140`; fx avg `-0.024` n `6`; index avg `0.0112` n `26`; metal avg `0.018` n `20`; unknown avg `0.2084` n `944`
- 1h: commodity avg `0.0519` n `12`; crypto_alt avg `-0.3923` n `234`; crypto_major avg `-0.3944` n `8`; equity avg `0.1262` n `140`; fx avg `-0.025` n `6`; index avg `0.0147` n `26`; metal avg `-0.0655` n `20`; unknown avg `0.1118` n `942`
- 4h: commodity avg `0.202` n `12`; crypto_alt avg `0.0866` n `234`; crypto_major avg `-0.8433` n `8`; equity avg `0.207` n `140`; fx avg `-0.1658` n `6`; index avg `0.0057` n `26`; metal avg `-0.1501` n `20`; unknown avg `0.8264` n `936`
- 24h: commodity avg `-0.0824` n `12`; crypto_alt avg `3.2031` n `234`; crypto_major avg `4.0789` n `8`; equity avg `2.5562` n `140`; fx avg `-0.2298` n `6`; index avg `0.4914` n `26`; metal avg `-0.0477` n `20`; unknown avg `8.3845` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
