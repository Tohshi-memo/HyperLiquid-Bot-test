# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T06:52:33.032516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `74.42` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.0899` n `234`; crypto_major avg `-0.0426` n `8`; equity avg `-0.0041` n `140`; fx avg `-0.0082` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0008` n `20`; unknown avg `-0.0593` n `943`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `-0.3641` n `234`; crypto_major avg `-0.0487` n `8`; equity avg `-0.0345` n `140`; fx avg `-0.0006` n `6`; index avg `-0.0012` n `26`; metal avg `0.0063` n `20`; unknown avg `0.2319` n `911`
- 4h: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.2897` n `234`; crypto_major avg `-0.198` n `8`; equity avg `-0.1791` n `140`; fx avg `-0.0096` n `6`; index avg `-0.0467` n `26`; metal avg `-0.0114` n `20`; unknown avg `1.1464` n `895`
- 24h: commodity avg `0.2359` n `12`; crypto_alt avg `-0.2139` n `234`; crypto_major avg `-1.8061` n `8`; equity avg `-0.1955` n `140`; fx avg `-0.0543` n `6`; index avg `-0.0144` n `26`; metal avg `0.0133` n `20`; unknown avg `0.6536` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
