# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T05:37:25.999930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0813` n `12`; crypto_alt avg `-0.2822` n `230`; crypto_major avg `-0.2654` n `8`; equity avg `-0.1386` n `114`; fx avg `0.0038` n `6`; index avg `-0.0354` n `25`; metal avg `-0.0496` n `20`; unknown avg `0.9216` n `793`
- 1h: commodity avg `-0.0432` n `12`; crypto_alt avg `-0.2813` n `230`; crypto_major avg `-0.2553` n `8`; equity avg `-0.3579` n `114`; fx avg `-0.0281` n `6`; index avg `-0.0788` n `25`; metal avg `-0.0257` n `20`; unknown avg `-0.0761` n `793`
- 4h: commodity avg `0.0055` n `12`; crypto_alt avg `-1.0763` n `230`; crypto_major avg `-0.4975` n `8`; equity avg `-1.5881` n `114`; fx avg `-0.015` n `6`; index avg `-0.31` n `25`; metal avg `-0.3085` n `20`; unknown avg `0.25` n `793`
- 24h: commodity avg `0.6506` n `12`; crypto_alt avg `-1.5536` n `230`; crypto_major avg `-0.1232` n `8`; equity avg `-1.4091` n `114`; fx avg `-0.0321` n `6`; index avg `-0.368` n `25`; metal avg `-0.2708` n `20`; unknown avg `0.0798` n `776`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
