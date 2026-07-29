# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T02:07:35.067446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.1394` n `230`; crypto_major avg `0.0102` n `8`; equity avg `-0.0694` n `102`; fx avg `-0.0193` n `6`; index avg `-0.0381` n `25`; metal avg `0.0184` n `20`; unknown avg `0.2311` n `777`
- 1h: commodity avg `0.0757` n `12`; crypto_alt avg `-0.6913` n `230`; crypto_major avg `-0.4261` n `8`; equity avg `-1.3645` n `102`; fx avg `-0.0123` n `6`; index avg `-0.3627` n `25`; metal avg `0.0393` n `20`; unknown avg `0.391` n `777`
- 4h: commodity avg `0.3286` n `12`; crypto_alt avg `-0.9833` n `230`; crypto_major avg `-0.5828` n `8`; equity avg `-1.3041` n `102`; fx avg `-0.018` n `6`; index avg `-0.3353` n `25`; metal avg `-0.0273` n `20`; unknown avg `0.5834` n `776`
- 24h: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.4547` n `230`; crypto_major avg `0.3802` n `8`; equity avg `-2.0824` n `102`; fx avg `-0.162` n `6`; index avg `-0.2914` n `25`; metal avg `-0.1212` n `20`; unknown avg `0.0238` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
