# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T17:07:28.477157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.061` n `12`; crypto_alt avg `0.0217` n `230`; crypto_major avg `0.0516` n `8`; equity avg `0.083` n `103`; fx avg `0.0065` n `6`; index avg `-0.0022` n `25`; metal avg `-0.047` n `20`; unknown avg `-0.031` n `784`
- 1h: commodity avg `0.0008` n `12`; crypto_alt avg `0.071` n `230`; crypto_major avg `0.0193` n `8`; equity avg `0.0603` n `103`; fx avg `-0.0064` n `6`; index avg `0.0077` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0922` n `784`
- 4h: commodity avg `0.1516` n `12`; crypto_alt avg `1.0237` n `230`; crypto_major avg `1.4242` n `8`; equity avg `2.5873` n `103`; fx avg `-0.0385` n `6`; index avg `0.2128` n `25`; metal avg `0.1038` n `20`; unknown avg `0.0542` n `784`
- 24h: commodity avg `-0.1518` n `12`; crypto_alt avg `0.3203` n `230`; crypto_major avg `0.9154` n `8`; equity avg `1.3401` n `102`; fx avg `-0.1762` n `6`; index avg `-0.0344` n `25`; metal avg `-0.4972` n `20`; unknown avg `0.1102` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
