# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T23:37:30.090063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `-0.2293` n `230`; crypto_major avg `-0.3274` n `8`; equity avg `-0.0224` n `108`; fx avg `-0.0022` n `6`; index avg `-0.025` n `25`; metal avg `-0.0218` n `20`; unknown avg `0.2374` n `781`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.102` n `230`; crypto_major avg `-0.1737` n `8`; equity avg `0.0883` n `108`; fx avg `0.0046` n `6`; index avg `0.0023` n `25`; metal avg `-0.1003` n `20`; unknown avg `0.0596` n `781`
- 4h: commodity avg `-0.0932` n `12`; crypto_alt avg `-0.1125` n `230`; crypto_major avg `-0.3558` n `8`; equity avg `-0.3696` n `108`; fx avg `0.0023` n `6`; index avg `-0.0678` n `25`; metal avg `-0.0753` n `20`; unknown avg `0.1906` n `781`
- 24h: commodity avg `-1.2175` n `12`; crypto_alt avg `0.1455` n `230`; crypto_major avg `0.6031` n `8`; equity avg `3.0099` n `107`; fx avg `0.0944` n `6`; index avg `0.6715` n `25`; metal avg `0.8356` n `20`; unknown avg `0.4226` n `764`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
