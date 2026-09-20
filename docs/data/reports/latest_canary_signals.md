# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T07:07:31.028070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `74.42` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0387` n `12`; crypto_alt avg `0.0628` n `234`; crypto_major avg `0.0597` n `8`; equity avg `0.0146` n `140`; fx avg `0.0034` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0016` n `20`; unknown avg `4.6126` n `941`
- 1h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.2425` n `234`; crypto_major avg `0.0754` n `8`; equity avg `-0.0057` n `140`; fx avg `-0.0147` n `6`; index avg `-0.009` n `26`; metal avg `0.0037` n `20`; unknown avg `4.5621` n `941`
- 4h: commodity avg `-0.0458` n `12`; crypto_alt avg `-0.1517` n `234`; crypto_major avg `-0.017` n `8`; equity avg `-0.0466` n `140`; fx avg `-0.0085` n `6`; index avg `-0.0194` n `26`; metal avg `0.0171` n `20`; unknown avg `1.0083` n `895`
- 24h: commodity avg `0.2037` n `12`; crypto_alt avg `-0.169` n `234`; crypto_major avg `-1.7615` n `8`; equity avg `-0.2023` n `140`; fx avg `-0.077` n `6`; index avg `-0.0439` n `26`; metal avg `0.0065` n `20`; unknown avg `4.6843` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
