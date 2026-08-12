# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T15:37:31.114162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.39` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7789` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `-0.0082` n `230`; crypto_major avg `0.117` n `8`; equity avg `-0.0662` n `113`; fx avg `0.0084` n `6`; index avg `-0.0045` n `25`; metal avg `-0.0554` n `20`; unknown avg `-0.0193` n `786`
- 1h: commodity avg `-0.001` n `12`; crypto_alt avg `0.052` n `230`; crypto_major avg `0.1972` n `8`; equity avg `0.1118` n `113`; fx avg `0.002` n `6`; index avg `-0.0353` n `25`; metal avg `-0.071` n `20`; unknown avg `-0.0505` n `786`
- 4h: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.3928` n `230`; crypto_major avg `-0.6273` n `8`; equity avg `1.1516` n `113`; fx avg `0.0037` n `6`; index avg `0.1159` n `25`; metal avg `-0.1794` n `20`; unknown avg `0.0308` n `786`
- 24h: commodity avg `0.1094` n `12`; crypto_alt avg `0.1825` n `230`; crypto_major avg `1.2495` n `8`; equity avg `3.1689` n `113`; fx avg `0.0391` n `6`; index avg `0.3465` n `25`; metal avg `0.3247` n `20`; unknown avg `0.0308` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2277`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2085`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
