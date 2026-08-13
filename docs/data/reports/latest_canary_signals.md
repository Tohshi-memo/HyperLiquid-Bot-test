# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T00:52:28.624063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.0285` n `230`; crypto_major avg `0.0236` n `8`; equity avg `0.0946` n `113`; fx avg `-0.0045` n `6`; index avg `0.0253` n `25`; metal avg `-0.0496` n `20`; unknown avg `0.0022` n `786`
- 1h: commodity avg `-0.1101` n `12`; crypto_alt avg `0.3911` n `230`; crypto_major avg `0.2083` n `8`; equity avg `0.2062` n `113`; fx avg `-0.0698` n `6`; index avg `0.0425` n `25`; metal avg `0.1565` n `20`; unknown avg `0.076` n `786`
- 4h: commodity avg `-0.0837` n `12`; crypto_alt avg `-0.1648` n `230`; crypto_major avg `-0.2002` n `8`; equity avg `0.3675` n `113`; fx avg `-0.0768` n `6`; index avg `0.047` n `25`; metal avg `0.1632` n `20`; unknown avg `-0.0826` n `786`
- 24h: commodity avg `-0.2233` n `12`; crypto_alt avg `-1.1586` n `230`; crypto_major avg `-0.4601` n `8`; equity avg `2.9543` n `113`; fx avg `-0.0543` n `6`; index avg `0.4156` n `25`; metal avg `0.2747` n `20`; unknown avg `0.0443` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2389`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
