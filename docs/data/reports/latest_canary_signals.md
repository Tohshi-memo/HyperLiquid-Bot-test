# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T13:37:30.205318+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0682` n `12`; crypto_alt avg `-0.4161` n `230`; crypto_major avg `-0.4722` n `8`; equity avg `0.0477` n `108`; fx avg `-0.0015` n `6`; index avg `0.0354` n `25`; metal avg `-0.0527` n `20`; unknown avg `-0.0804` n `782`
- 1h: commodity avg `-0.1478` n `12`; crypto_alt avg `-0.6227` n `230`; crypto_major avg `-0.7949` n `8`; equity avg `-0.3434` n `108`; fx avg `0.0043` n `6`; index avg `0.0184` n `25`; metal avg `-0.1314` n `20`; unknown avg `-0.065` n `782`
- 4h: commodity avg `-0.134` n `12`; crypto_alt avg `-0.536` n `230`; crypto_major avg `-0.6717` n `8`; equity avg `-0.2366` n `108`; fx avg `-0.001` n `6`; index avg `0.0693` n `25`; metal avg `-0.015` n `20`; unknown avg `-0.1373` n `781`
- 24h: commodity avg `-0.0276` n `12`; crypto_alt avg `0.1091` n `230`; crypto_major avg `-0.2353` n `8`; equity avg `1.1671` n `108`; fx avg `0.0819` n `6`; index avg `0.4749` n `25`; metal avg `0.5619` n `20`; unknown avg `-0.0637` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
