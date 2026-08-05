# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T01:22:27.557441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `0.2383` n `230`; crypto_major avg `0.156` n `8`; equity avg `-0.1694` n `108`; fx avg `0.0147` n `6`; index avg `-0.0371` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.0473` n `781`
- 1h: commodity avg `0.1497` n `12`; crypto_alt avg `0.2129` n `230`; crypto_major avg `0.1823` n `8`; equity avg `-0.3054` n `108`; fx avg `-0.0239` n `6`; index avg `-0.0752` n `25`; metal avg `-0.026` n `20`; unknown avg `0.0377` n `781`
- 4h: commodity avg `0.1819` n `12`; crypto_alt avg `-0.0392` n `230`; crypto_major avg `-0.2072` n `8`; equity avg `0.2234` n `108`; fx avg `-0.0545` n `6`; index avg `0.0273` n `25`; metal avg `-0.0255` n `20`; unknown avg `0.0324` n `781`
- 24h: commodity avg `-1.1743` n `12`; crypto_alt avg `0.3834` n `230`; crypto_major avg `0.693` n `8`; equity avg `3.7199` n `107`; fx avg `0.0907` n `6`; index avg `0.8643` n `25`; metal avg `0.8338` n `20`; unknown avg `0.3986` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
