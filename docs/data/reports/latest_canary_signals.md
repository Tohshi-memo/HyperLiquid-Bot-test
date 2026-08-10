# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T10:52:39.458136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0441` n `12`; crypto_alt avg `0.1296` n `230`; crypto_major avg `0.0872` n `8`; equity avg `0.0118` n `113`; fx avg `-0.0038` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0104` n `20`; unknown avg `0.0244` n `784`
- 1h: commodity avg `0.0707` n `12`; crypto_alt avg `0.1504` n `230`; crypto_major avg `0.1204` n `8`; equity avg `-0.0516` n `113`; fx avg `-0.0138` n `6`; index avg `-0.0103` n `25`; metal avg `-0.0194` n `20`; unknown avg `0.0683` n `784`
- 4h: commodity avg `0.345` n `12`; crypto_alt avg `0.066` n `230`; crypto_major avg `-0.011` n `8`; equity avg `-0.0247` n `113`; fx avg `0.0198` n `6`; index avg `-0.0013` n `25`; metal avg `-0.1208` n `20`; unknown avg `0.05` n `784`
- 24h: commodity avg `0.491` n `12`; crypto_alt avg `0.949` n `230`; crypto_major avg `0.0063` n `8`; equity avg `-0.1363` n `113`; fx avg `0.2142` n `6`; index avg `0.0585` n `25`; metal avg `-0.1448` n `20`; unknown avg `56.9708` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
