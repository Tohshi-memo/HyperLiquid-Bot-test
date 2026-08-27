# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T12:22:30.574413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0419` n `12`; crypto_alt avg `0.1543` n `231`; crypto_major avg `0.1298` n `8`; equity avg `0.0528` n `127`; fx avg `-0.0052` n `6`; index avg `0.0062` n `26`; metal avg `-0.0082` n `20`; unknown avg `0.0525` n `792`
- 1h: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.0352` n `231`; crypto_major avg `-0.1721` n `8`; equity avg `-0.1127` n `127`; fx avg `-0.0046` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.0597` n `792`
- 4h: commodity avg `0.2059` n `12`; crypto_alt avg `-0.1758` n `231`; crypto_major avg `0.1042` n `8`; equity avg `-0.1997` n `127`; fx avg `0.0023` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0521` n `20`; unknown avg `0.0304` n `792`
- 24h: commodity avg `0.4786` n `12`; crypto_alt avg `1.187` n `231`; crypto_major avg `1.7154` n `8`; equity avg `1.8902` n `127`; fx avg `-0.0968` n `6`; index avg `0.2936` n `26`; metal avg `-0.3384` n `20`; unknown avg `0.5763` n `775`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
