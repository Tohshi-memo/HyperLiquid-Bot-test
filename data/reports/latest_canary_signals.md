# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T18:12:53.712982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0283` n `12`; crypto_alt avg `-0.0237` n `232`; crypto_major avg `0.4959` n `8`; equity avg `-0.0061` n `134`; fx avg `-0.0033` n `6`; index avg `0.0016` n `26`; metal avg `-0.0032` n `20`; unknown avg `19.0788` n `792`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `-0.0974` n `232`; crypto_major avg `0.6503` n `8`; equity avg `0.0347` n `134`; fx avg `-0.0226` n `6`; index avg `0.0069` n `26`; metal avg `0.0089` n `20`; unknown avg `0.1629` n `792`
- 4h: commodity avg `0.0608` n `12`; crypto_alt avg `0.4902` n `232`; crypto_major avg `1.4917` n `8`; equity avg `0.1336` n `134`; fx avg `-0.0259` n `6`; index avg `0.0345` n `26`; metal avg `0.0357` n `20`; unknown avg `-0.7869` n `786`
- 24h: commodity avg `0.02` n `12`; crypto_alt avg `2.6486` n `232`; crypto_major avg `3.157` n `8`; equity avg `0.5661` n `134`; fx avg `-0.0213` n `6`; index avg `0.0858` n `26`; metal avg `0.1954` n `20`; unknown avg `0.185` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
