# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T13:22:28.567049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0401` n `12`; crypto_alt avg `0.3351` n `230`; crypto_major avg `0.3702` n `8`; equity avg `0.1163` n `94`; fx avg `-0.0149` n `6`; index avg `0.0327` n `25`; metal avg `0.146` n `20`; unknown avg `0.1169` n `768`
- 1h: commodity avg `-0.0032` n `12`; crypto_alt avg `0.3299` n `230`; crypto_major avg `0.0945` n `8`; equity avg `0.0561` n `94`; fx avg `-0.0039` n `6`; index avg `0.0358` n `25`; metal avg `-0.0775` n `20`; unknown avg `-0.0239` n `768`
- 4h: commodity avg `0.3811` n `12`; crypto_alt avg `0.3878` n `230`; crypto_major avg `0.0769` n `8`; equity avg `-0.688` n `94`; fx avg `-0.0072` n `6`; index avg `-0.1587` n `25`; metal avg `-0.2844` n `20`; unknown avg `0.0894` n `768`
- 24h: commodity avg `0.2384` n `12`; crypto_alt avg `-1.6453` n `230`; crypto_major avg `-2.2746` n `8`; equity avg `-3.3141` n `93`; fx avg `0.0273` n `6`; index avg `-0.5706` n `25`; metal avg `-0.4826` n `20`; unknown avg `-0.0942` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
