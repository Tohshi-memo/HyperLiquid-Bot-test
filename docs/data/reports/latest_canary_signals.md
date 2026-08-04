# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T14:07:34.238104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.1189` n `230`; crypto_major avg `-0.0357` n `8`; equity avg `0.0383` n `107`; fx avg `-0.0088` n `6`; index avg `0.0077` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.0366` n `782`
- 1h: commodity avg `-0.4258` n `12`; crypto_alt avg `-0.2217` n `230`; crypto_major avg `-0.3545` n `8`; equity avg `0.609` n `107`; fx avg `-0.0326` n `6`; index avg `0.1917` n `25`; metal avg `0.2175` n `20`; unknown avg `-0.1646` n `781`
- 4h: commodity avg `-1.3691` n `12`; crypto_alt avg `-0.2447` n `230`; crypto_major avg `0.3128` n `8`; equity avg `1.4532` n `107`; fx avg `-0.1098` n `6`; index avg `0.3562` n `25`; metal avg `0.6044` n `20`; unknown avg `-0.149` n `781`
- 24h: commodity avg `-0.9005` n `12`; crypto_alt avg `-0.1286` n `230`; crypto_major avg `0.658` n `8`; equity avg `4.9626` n `107`; fx avg `0.0433` n `6`; index avg `0.8659` n `25`; metal avg `1.156` n `20`; unknown avg `0.566` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
