# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T14:52:29.795532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `12`; crypto_alt avg `0.4031` n `234`; crypto_major avg `0.2952` n `8`; equity avg `-0.0679` n `140`; fx avg `0.0062` n `6`; index avg `-0.0073` n `26`; metal avg `0.0242` n `20`; unknown avg `0.0731` n `942`
- 1h: commodity avg `-0.1952` n `12`; crypto_alt avg `0.3102` n `234`; crypto_major avg `0.3894` n `8`; equity avg `0.2628` n `140`; fx avg `0.0022` n `6`; index avg `0.0759` n `26`; metal avg `-0.1228` n `20`; unknown avg `0.6991` n `882`
- 4h: commodity avg `-0.159` n `12`; crypto_alt avg `0.7421` n `234`; crypto_major avg `1.4596` n `8`; equity avg `0.4574` n `140`; fx avg `0.0134` n `6`; index avg `0.1274` n `26`; metal avg `0.0353` n `20`; unknown avg `11.1869` n `856`
- 24h: commodity avg `-1.0198` n `12`; crypto_alt avg `7.4634` n `234`; crypto_major avg `6.7034` n `8`; equity avg `2.5187` n `140`; fx avg `-0.0887` n `6`; index avg `0.4902` n `26`; metal avg `0.0252` n `20`; unknown avg `3.7951` n `707`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
