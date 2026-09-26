# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T00:07:30.219815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.0734` n `234`; crypto_major avg `-0.0804` n `8`; equity avg `0.0238` n `141`; fx avg `0.0013` n `6`; index avg `-0.0004` n `26`; metal avg `0.0035` n `20`; unknown avg `0.1407` n `952`
- 1h: commodity avg `-0.0111` n `12`; crypto_alt avg `0.0806` n `234`; crypto_major avg `-0.1193` n `8`; equity avg `-0.0135` n `141`; fx avg `-0.0062` n `6`; index avg `0.003` n `26`; metal avg `0.0055` n `20`; unknown avg `0.2761` n `952`
- 4h: commodity avg `0.0244` n `12`; crypto_alt avg `0.7284` n `234`; crypto_major avg `0.273` n `8`; equity avg `0.0843` n `141`; fx avg `-0.0176` n `6`; index avg `0.0183` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.3706` n `874`
- 24h: commodity avg `-0.3376` n `12`; crypto_alt avg `2.7655` n `234`; crypto_major avg `0.918` n `8`; equity avg `0.1568` n `141`; fx avg `-0.247` n `6`; index avg `0.2552` n `26`; metal avg `0.1978` n `20`; unknown avg `1125.049` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
