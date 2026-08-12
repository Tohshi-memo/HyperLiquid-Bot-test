# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T15:07:29.745079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.23` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.8142` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `0.1842` n `230`; crypto_major avg `0.0429` n `8`; equity avg `0.0758` n `113`; fx avg `0.0035` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.0332` n `786`
- 1h: commodity avg `0.0614` n `12`; crypto_alt avg `-0.1566` n `230`; crypto_major avg `-0.0312` n `8`; equity avg `0.0904` n `113`; fx avg `-0.0164` n `6`; index avg `-0.0127` n `25`; metal avg `-0.0647` n `20`; unknown avg `-0.0724` n `786`
- 4h: commodity avg `0.0278` n `12`; crypto_alt avg `-0.3763` n `230`; crypto_major avg `-0.7171` n `8`; equity avg `1.0971` n `113`; fx avg `0.007` n `6`; index avg `0.1169` n `25`; metal avg `-0.1119` n `20`; unknown avg `-0.001` n `786`
- 24h: commodity avg `0.231` n `12`; crypto_alt avg `-0.5268` n `230`; crypto_major avg `0.69` n `8`; equity avg `3.0493` n `113`; fx avg `0.043` n `6`; index avg `0.3009` n `25`; metal avg `0.221` n `20`; unknown avg `-0.0595` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2112`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
