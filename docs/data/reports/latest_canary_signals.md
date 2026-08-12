# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T20:58:53.105527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.032` n `12`; crypto_alt avg `-0.1571` n `230`; crypto_major avg `-0.0609` n `8`; equity avg `0.0413` n `113`; fx avg `0.0009` n `6`; index avg `0.0011` n `25`; metal avg `-0.0091` n `20`; unknown avg `-0.1544` n `786`
- 1h: commodity avg `-0.0814` n `12`; crypto_alt avg `0.1257` n `230`; crypto_major avg `0.2202` n `8`; equity avg `-0.2258` n `113`; fx avg `-0.0003` n `6`; index avg `0.0011` n `25`; metal avg `-0.0148` n `20`; unknown avg `0.532` n `786`
- 4h: commodity avg `-0.0713` n `12`; crypto_alt avg `-0.1783` n `230`; crypto_major avg `-0.0383` n `8`; equity avg `-0.0723` n `113`; fx avg `0.0054` n `6`; index avg `0.0102` n `25`; metal avg `-0.007` n `20`; unknown avg `0.3162` n `786`
- 24h: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.7694` n `230`; crypto_major avg `0.1336` n `8`; equity avg `2.874` n `113`; fx avg `0.0396` n `6`; index avg `0.3801` n `25`; metal avg `0.1726` n `20`; unknown avg `0.0128` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2329`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2018`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
