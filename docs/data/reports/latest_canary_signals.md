# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T11:52:32.190693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.0061` n `228`; crypto_major avg `-0.0102` n `8`; equity avg `0.036` n `74`; fx avg `-0.0024` n `6`; index avg `0.0083` n `23`; metal avg `0.0232` n `18`; unknown avg `0.0138` n `645`
- 1h: commodity avg `0.0663` n `12`; crypto_alt avg `-0.0744` n `228`; crypto_major avg `0.0292` n `8`; equity avg `0.1127` n `74`; fx avg `0.0091` n `6`; index avg `0.0564` n `23`; metal avg `-0.0193` n `18`; unknown avg `-0.0851` n `645`
- 4h: commodity avg `0.2692` n `12`; crypto_alt avg `0.0843` n `228`; crypto_major avg `0.3249` n `8`; equity avg `0.3806` n `74`; fx avg `0.0106` n `6`; index avg `0.1293` n `23`; metal avg `-0.024` n `18`; unknown avg `0.3573` n `629`
- 24h: commodity avg `-0.4756` n `12`; crypto_alt avg `-0.0276` n `228`; crypto_major avg `0.8227` n `8`; equity avg `1.1066` n `74`; fx avg `-0.0055` n `6`; index avg `0.2833` n `23`; metal avg `0.1171` n `18`; unknown avg `-0.943` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
