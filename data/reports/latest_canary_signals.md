# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T06:01:33.508816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0464` n `12`; crypto_alt avg `-0.1011` n `231`; crypto_major avg `-0.1706` n `8`; equity avg `0.0386` n `122`; fx avg `-0.01` n `6`; index avg `0.0115` n `25`; metal avg `0.018` n `20`; unknown avg `-0.0614` n `778`
- 1h: commodity avg `-0.1674` n `12`; crypto_alt avg `0.0374` n `231`; crypto_major avg `-0.0138` n `8`; equity avg `0.2457` n `122`; fx avg `0.0277` n `6`; index avg `0.045` n `25`; metal avg `-0.0107` n `20`; unknown avg `-0.0806` n `778`
- 4h: commodity avg `-0.2992` n `12`; crypto_alt avg `1.12` n `231`; crypto_major avg `1.0081` n `8`; equity avg `0.955` n `122`; fx avg `0.0113` n `6`; index avg `0.1753` n `25`; metal avg `-0.0907` n `20`; unknown avg `0.0358` n `778`
- 24h: commodity avg `-0.1699` n `12`; crypto_alt avg `2.2477` n `231`; crypto_major avg `3.0853` n `8`; equity avg `0.3116` n `122`; fx avg `0.0468` n `6`; index avg `0.0387` n `25`; metal avg `-0.208` n `20`; unknown avg `0.5404` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
