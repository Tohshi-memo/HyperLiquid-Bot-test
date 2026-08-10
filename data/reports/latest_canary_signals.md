# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T14:37:29.255654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `-0.0017` n `230`; crypto_major avg `0.0855` n `8`; equity avg `0.0957` n `113`; fx avg `0.0189` n `6`; index avg `0.0203` n `25`; metal avg `0.0813` n `20`; unknown avg `0.0991` n `784`
- 1h: commodity avg `0.1313` n `12`; crypto_alt avg `-0.0807` n `230`; crypto_major avg `0.0803` n `8`; equity avg `0.3556` n `113`; fx avg `0.0196` n `6`; index avg `0.0757` n `25`; metal avg `0.1019` n `20`; unknown avg `0.2434` n `784`
- 4h: commodity avg `0.3733` n `12`; crypto_alt avg `0.0184` n `230`; crypto_major avg `-0.1641` n `8`; equity avg `-0.4637` n `113`; fx avg `0.0412` n `6`; index avg `-0.0117` n `25`; metal avg `0.0775` n `20`; unknown avg `0.1667` n `784`
- 24h: commodity avg `0.9895` n `12`; crypto_alt avg `0.4204` n `230`; crypto_major avg `-0.5146` n `8`; equity avg `-0.7349` n `113`; fx avg `0.2623` n `6`; index avg `0.0306` n `25`; metal avg `-0.0788` n `20`; unknown avg `59.0161` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
