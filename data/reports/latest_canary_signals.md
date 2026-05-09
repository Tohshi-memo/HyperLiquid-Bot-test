# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T11:22:14.215461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `0.008` n `228`; crypto_major avg `0.1094` n `8`; equity avg `-0.0077` n `65`; fx avg `0.0025` n `5`; index avg `0.0028` n `23`; metal avg `0.0112` n `18`; unknown avg `0.0114` n `376`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `0.3787` n `228`; crypto_major avg `0.2356` n `8`; equity avg `0.0294` n `65`; fx avg `0.0055` n `5`; index avg `-0.0119` n `23`; metal avg `0.0057` n `18`; unknown avg `-0.216` n `376`
- 4h: commodity avg `0.0152` n `12`; crypto_alt avg `-0.4006` n `228`; crypto_major avg `-0.163` n `8`; equity avg `0.0849` n `65`; fx avg `0.0096` n `5`; index avg `-0.0182` n `23`; metal avg `-0.0415` n `18`; unknown avg `-0.4586` n `376`
- 24h: commodity avg `-0.1518` n `12`; crypto_alt avg `3.1425` n `228`; crypto_major avg `1.9885` n `8`; equity avg `2.8721` n `65`; fx avg `0.0037` n `5`; index avg `1.1445` n `23`; metal avg `-0.1955` n `18`; unknown avg `0.4763` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
