# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T21:52:25.585165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `12`; crypto_alt avg `0.0735` n `230`; crypto_major avg `0.1127` n `8`; equity avg `-0.0159` n `113`; fx avg `-0.0014` n `6`; index avg `0.004` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.0063` n `786`
- 1h: commodity avg `0.0404` n `12`; crypto_alt avg `-0.4975` n `230`; crypto_major avg `-0.2807` n `8`; equity avg `0.0742` n `113`; fx avg `-0.0146` n `6`; index avg `0.0196` n `25`; metal avg `-0.0124` n `20`; unknown avg `-0.1036` n `786`
- 4h: commodity avg `-0.0404` n `12`; crypto_alt avg `-0.8686` n `230`; crypto_major avg `-0.5109` n `8`; equity avg `-0.3788` n `113`; fx avg `-0.0151` n `6`; index avg `0.0067` n `25`; metal avg `-0.0474` n `20`; unknown avg `-0.3096` n `786`
- 24h: commodity avg `0.034` n `12`; crypto_alt avg `-1.3707` n `230`; crypto_major avg `-0.3992` n `8`; equity avg `2.9089` n `113`; fx avg `0.0221` n `6`; index avg `0.4032` n `25`; metal avg `0.1596` n `20`; unknown avg `-0.0281` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2349`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
