# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T08:37:26.080521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.115` n `232`; crypto_major avg `-0.0985` n `8`; equity avg `-0.018` n `134`; fx avg `-0.0019` n `6`; index avg `-0.003` n `26`; metal avg `0.002` n `20`; unknown avg `-0.0376` n `788`
- 1h: commodity avg `0.0155` n `12`; crypto_alt avg `0.153` n `232`; crypto_major avg `0.093` n `8`; equity avg `0.0303` n `134`; fx avg `-0.0243` n `6`; index avg `-0.0143` n `26`; metal avg `-0.001` n `20`; unknown avg `-0.163` n `786`
- 4h: commodity avg `0.0182` n `12`; crypto_alt avg `-0.1798` n `232`; crypto_major avg `-0.2214` n `8`; equity avg `0.0479` n `134`; fx avg `0.0208` n `6`; index avg `-0.0101` n `26`; metal avg `-0.0073` n `20`; unknown avg `0.1407` n `758`
- 24h: commodity avg `0.1462` n `12`; crypto_alt avg `1.6837` n `232`; crypto_major avg `1.8161` n `8`; equity avg `0.4218` n `134`; fx avg `-0.0398` n `6`; index avg `0.0873` n `26`; metal avg `0.0015` n `20`; unknown avg `493.2193` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
