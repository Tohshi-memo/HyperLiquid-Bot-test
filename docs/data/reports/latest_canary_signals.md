# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T07:37:27.765940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `0.0302` n `230`; crypto_major avg `-0.0005` n `8`; equity avg `-0.1726` n `108`; fx avg `0.0103` n `6`; index avg `-0.0318` n `25`; metal avg `-0.0275` n `20`; unknown avg `0.0129` n `781`
- 1h: commodity avg `0.1897` n `12`; crypto_alt avg `-0.2459` n `230`; crypto_major avg `-0.4225` n `8`; equity avg `-0.349` n `108`; fx avg `0.0262` n `6`; index avg `-0.0527` n `25`; metal avg `-0.043` n `20`; unknown avg `-0.0213` n `781`
- 4h: commodity avg `0.387` n `12`; crypto_alt avg `0.216` n `230`; crypto_major avg `0.1003` n `8`; equity avg `-0.0834` n `108`; fx avg `0.047` n `6`; index avg `-0.02` n `25`; metal avg `0.3064` n `20`; unknown avg `0.1166` n `749`
- 24h: commodity avg `-1.1382` n `12`; crypto_alt avg `0.5672` n `230`; crypto_major avg `0.5536` n `8`; equity avg `2.9985` n `108`; fx avg `-0.0096` n `6`; index avg `0.6597` n `25`; metal avg `1.2157` n `20`; unknown avg `0.1084` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
