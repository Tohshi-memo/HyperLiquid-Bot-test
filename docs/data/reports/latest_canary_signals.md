# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T04:22:23.378600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.094` n `12`; crypto_alt avg `0.0599` n `230`; crypto_major avg `-0.0375` n `8`; equity avg `-0.1555` n `108`; fx avg `0.0137` n `6`; index avg `-0.0395` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.0488` n `781`
- 1h: commodity avg `0.1065` n `12`; crypto_alt avg `0.2376` n `230`; crypto_major avg `-0.0005` n `8`; equity avg `0.022` n `108`; fx avg `0.0167` n `6`; index avg `-0.014` n `25`; metal avg `0.0222` n `20`; unknown avg `-0.0237` n `781`
- 4h: commodity avg `-0.0342` n `12`; crypto_alt avg `0.533` n `230`; crypto_major avg `0.3299` n `8`; equity avg `0.3846` n `108`; fx avg `-0.0675` n `6`; index avg `-0.0389` n `25`; metal avg `0.4172` n `20`; unknown avg `-0.1567` n `781`
- 24h: commodity avg `-1.4307` n `12`; crypto_alt avg `0.2495` n `230`; crypto_major avg `0.345` n `8`; equity avg `3.9382` n `108`; fx avg `-0.0382` n `6`; index avg `0.8017` n `25`; metal avg `1.0618` n `20`; unknown avg `0.393` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
