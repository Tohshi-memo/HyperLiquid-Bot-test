# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T20:37:29.541078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.3023` n `232`; crypto_major avg `-0.4122` n `8`; equity avg `0.0176` n `129`; fx avg `0.0026` n `6`; index avg `-0.0063` n `26`; metal avg `0.0023` n `20`; unknown avg `2.172` n `793`
- 1h: commodity avg `0.0703` n `12`; crypto_alt avg `-0.0041` n `232`; crypto_major avg `-0.1714` n `8`; equity avg `0.316` n `129`; fx avg `-0.0019` n `6`; index avg `0.0484` n `26`; metal avg `0.0135` n `20`; unknown avg `2.4138` n `779`
- 4h: commodity avg `0.0761` n `12`; crypto_alt avg `0.4172` n `232`; crypto_major avg `0.5849` n `8`; equity avg `0.4421` n `129`; fx avg `0.0033` n `6`; index avg `0.0529` n `26`; metal avg `0.0774` n `20`; unknown avg `-0.0146` n `779`
- 24h: commodity avg `0.2017` n `12`; crypto_alt avg `-0.8548` n `231`; crypto_major avg `-0.8294` n `8`; equity avg `0.024` n `129`; fx avg `-0.092` n `6`; index avg `-0.1438` n `26`; metal avg `-0.4364` n `20`; unknown avg `-0.0814` n `746`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
