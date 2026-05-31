# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T19:07:23.180017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0317` n `12`; crypto_alt avg `-0.0716` n `228`; crypto_major avg `-0.0337` n `8`; equity avg `-0.0521` n `69`; fx avg `-0.004` n `6`; index avg `0.0398` n `23`; metal avg `0.0044` n `18`; unknown avg `-0.2542` n `421`
- 1h: commodity avg `0.0417` n `12`; crypto_alt avg `-0.08` n `228`; crypto_major avg `-0.1547` n `8`; equity avg `-0.0006` n `69`; fx avg `-0.0063` n `6`; index avg `0.0184` n `23`; metal avg `0.0149` n `18`; unknown avg `-0.0459` n `421`
- 4h: commodity avg `0.1905` n `12`; crypto_alt avg `0.0509` n `228`; crypto_major avg `-0.3198` n `8`; equity avg `0.0706` n `69`; fx avg `-0.0146` n `6`; index avg `0.3546` n `23`; metal avg `-0.0383` n `18`; unknown avg `-0.1177` n `421`
- 24h: commodity avg `0.7537` n `12`; crypto_alt avg `-1.4276` n `228`; crypto_major avg `-0.9013` n `8`; equity avg `0.8798` n `69`; fx avg `-0.0267` n `6`; index avg `0.1662` n `23`; metal avg `-0.1287` n `18`; unknown avg `0.1111` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2381`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
