# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T01:42:46.309334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `-0.006` n `228`; crypto_major avg `-0.1562` n `8`; equity avg `-0.2058` n `74`; fx avg `0.0344` n `6`; index avg `-0.1569` n `23`; metal avg `0.0413` n `18`; unknown avg `0.2047` n `556`
- 1h: commodity avg `-0.042` n `12`; crypto_alt avg `-0.6236` n `228`; crypto_major avg `-0.6489` n `8`; equity avg `-0.7051` n `74`; fx avg `0.0213` n `6`; index avg `-0.2559` n `23`; metal avg `-0.522` n `18`; unknown avg `0.0479` n `556`
- 4h: commodity avg `0.0926` n `12`; crypto_alt avg `-0.5521` n `228`; crypto_major avg `-0.4262` n `8`; equity avg `0.2319` n `74`; fx avg `0.0123` n `6`; index avg `0.0083` n `23`; metal avg `-0.1957` n `18`; unknown avg `6.2243` n `556`
- 24h: commodity avg `-2.2602` n `12`; crypto_alt avg `2.7056` n `228`; crypto_major avg `2.7934` n `8`; equity avg `3.3591` n `74`; fx avg `-0.0262` n `6`; index avg `1.8724` n `23`; metal avg `2.1421` n `18`; unknown avg `2.645` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
