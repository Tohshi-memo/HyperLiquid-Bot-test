# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T01:37:32.641447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.4612` n `228`; crypto_major avg `-0.4734` n `8`; equity avg `-0.3637` n `86`; fx avg `-0.0053` n `6`; index avg `-0.0946` n `23`; metal avg `-0.1304` n `20`; unknown avg `-0.4698` n `765`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.7088` n `228`; crypto_major avg `-0.9181` n `8`; equity avg `-0.3738` n `86`; fx avg `0.0034` n `6`; index avg `-0.0479` n `23`; metal avg `-0.0938` n `20`; unknown avg `-1.0123` n `765`
- 4h: commodity avg `0.0524` n `12`; crypto_alt avg `-0.738` n `228`; crypto_major avg `-0.8973` n `8`; equity avg `-0.9889` n `86`; fx avg `0.0416` n `6`; index avg `-0.1763` n `23`; metal avg `-0.2548` n `20`; unknown avg `-0.6085` n `749`
- 24h: commodity avg `0.5119` n `12`; crypto_alt avg `-1.7631` n `228`; crypto_major avg `-2.0598` n `8`; equity avg `-2.8507` n `86`; fx avg `0.0582` n `6`; index avg `-0.3113` n `23`; metal avg `0.3876` n `20`; unknown avg `0.4446` n `700`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
