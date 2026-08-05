# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T10:37:29.248491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0483` n `12`; crypto_alt avg `0.0726` n `230`; crypto_major avg `0.1043` n `8`; equity avg `0.0168` n `108`; fx avg `-0.0118` n `6`; index avg `0.0058` n `25`; metal avg `-0.0468` n `20`; unknown avg `0.041` n `782`
- 1h: commodity avg `0.0382` n `12`; crypto_alt avg `-0.0612` n `230`; crypto_major avg `-0.1824` n `8`; equity avg `-0.0682` n `108`; fx avg `0.0128` n `6`; index avg `-0.0217` n `25`; metal avg `-0.0878` n `20`; unknown avg `0.005` n `781`
- 4h: commodity avg `0.2079` n `12`; crypto_alt avg `-0.231` n `230`; crypto_major avg `-0.2196` n `8`; equity avg `-0.7052` n `108`; fx avg `0.0493` n `6`; index avg `-0.0979` n `25`; metal avg `-0.2761` n `20`; unknown avg `0.6636` n `781`
- 24h: commodity avg `-1.1986` n `12`; crypto_alt avg `0.8437` n `230`; crypto_major avg `0.9614` n `8`; equity avg `2.4275` n `108`; fx avg `-0.0008` n `6`; index avg `0.6204` n `25`; metal avg `1.0142` n `20`; unknown avg `0.1709` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
