# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T09:07:36.620214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0738` n `12`; crypto_alt avg `0.0099` n `230`; crypto_major avg `-0.0016` n `8`; equity avg `0.1311` n `108`; fx avg `0.0016` n `6`; index avg `-0.0033` n `25`; metal avg `0.0772` n `20`; unknown avg `-0.0346` n `781`
- 1h: commodity avg `0.0396` n `12`; crypto_alt avg `-0.1359` n `230`; crypto_major avg `0.0927` n `8`; equity avg `-0.5722` n `108`; fx avg `-0.0159` n `6`; index avg `-0.0758` n `25`; metal avg `-0.1086` n `20`; unknown avg `-0.0306` n `781`
- 4h: commodity avg `0.2164` n `12`; crypto_alt avg `-0.0943` n `230`; crypto_major avg `0.0729` n `8`; equity avg `-0.8222` n `108`; fx avg `0.0017` n `6`; index avg `-0.1098` n `25`; metal avg `0.1815` n `20`; unknown avg `0.0838` n `749`
- 24h: commodity avg `-1.3927` n `12`; crypto_alt avg `0.5808` n `230`; crypto_major avg `1.1193` n `8`; equity avg `2.7508` n `108`; fx avg `-0.0311` n `6`; index avg `0.687` n `25`; metal avg `1.2143` n `20`; unknown avg `0.1006` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
