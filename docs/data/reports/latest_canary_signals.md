# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T08:52:27.038709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0314` n `12`; crypto_alt avg `-0.166` n `230`; crypto_major avg `-0.0643` n `8`; equity avg `-0.0056` n `108`; fx avg `-0.0175` n `6`; index avg `0.0072` n `25`; metal avg `-0.0881` n `20`; unknown avg `-0.0161` n `781`
- 1h: commodity avg `0.0813` n `12`; crypto_alt avg `-0.0585` n `230`; crypto_major avg `0.259` n `8`; equity avg `-0.5436` n `108`; fx avg `0.0066` n `6`; index avg `-0.0606` n `25`; metal avg `-0.2111` n `20`; unknown avg `0.0585` n `781`
- 4h: commodity avg `0.3107` n `12`; crypto_alt avg `0.0871` n `230`; crypto_major avg `0.4149` n `8`; equity avg `-0.7645` n `108`; fx avg `0.0204` n `6`; index avg `-0.0864` n `25`; metal avg `0.1184` n `20`; unknown avg `0.1335` n `749`
- 24h: commodity avg `-1.3257` n `12`; crypto_alt avg `0.5348` n `230`; crypto_major avg `0.984` n `8`; equity avg `2.3854` n `108`; fx avg `-0.0262` n `6`; index avg `0.6243` n `25`; metal avg `1.084` n `20`; unknown avg `0.1452` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
