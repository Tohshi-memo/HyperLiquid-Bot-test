# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T20:22:33.582694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `-0.0792` n `230`; crypto_major avg `-0.0612` n `8`; equity avg `-0.3325` n `113`; fx avg `-0.0034` n `6`; index avg `-0.0218` n `25`; metal avg `-0.0318` n `20`; unknown avg `-0.0448` n `786`
- 1h: commodity avg `-0.0381` n `12`; crypto_alt avg `-0.0176` n `230`; crypto_major avg `-0.1235` n `8`; equity avg `-0.3454` n `113`; fx avg `-0.0001` n `6`; index avg `-0.0095` n `25`; metal avg `-0.0786` n `20`; unknown avg `-0.0711` n `786`
- 4h: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.3494` n `230`; crypto_major avg `-0.2339` n `8`; equity avg `-0.1903` n `113`; fx avg `0.0` n `6`; index avg `0.0193` n `25`; metal avg `-0.1598` n `20`; unknown avg `0.2696` n `786`
- 24h: commodity avg `0.0263` n `12`; crypto_alt avg `-0.8883` n `230`; crypto_major avg `-0.0733` n `8`; equity avg `2.8525` n `113`; fx avg `0.0313` n `6`; index avg `0.3773` n `25`; metal avg `0.1737` n `20`; unknown avg `0.0223` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2321`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2063`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
