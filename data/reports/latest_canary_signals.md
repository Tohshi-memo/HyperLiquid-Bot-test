# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T20:07:40.317971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `0.1854` n `230`; crypto_major avg `0.1307` n `8`; equity avg `0.0462` n `113`; fx avg `0.0024` n `6`; index avg `0.0274` n `25`; metal avg `0.0164` n `20`; unknown avg `0.609` n `786`
- 1h: commodity avg `-0.0471` n `12`; crypto_alt avg `-0.0937` n `230`; crypto_major avg `-0.1388` n `8`; equity avg `-0.0593` n `113`; fx avg `0.0069` n `6`; index avg `0.0022` n `25`; metal avg `-0.0491` n `20`; unknown avg `-0.0912` n `786`
- 4h: commodity avg `-0.0401` n `12`; crypto_alt avg `-0.2493` n `230`; crypto_major avg `-0.1888` n `8`; equity avg `0.2649` n `113`; fx avg `0.0002` n `6`; index avg `0.0543` n `25`; metal avg `-0.1099` n `20`; unknown avg `0.3832` n `786`
- 24h: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.8921` n `230`; crypto_major avg `-0.089` n `8`; equity avg `3.5439` n `113`; fx avg `0.0284` n `6`; index avg `0.4271` n `25`; metal avg `0.1947` n `20`; unknown avg `0.094` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2316`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2063`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
