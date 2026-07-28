# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T23:37:27.006803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `0.1991` n `230`; crypto_major avg `0.2623` n `8`; equity avg `0.2231` n `102`; fx avg `0.0` n `6`; index avg `0.0434` n `25`; metal avg `0.0083` n `20`; unknown avg `0.0769` n `776`
- 1h: commodity avg `0.0127` n `12`; crypto_alt avg `-0.181` n `230`; crypto_major avg `-0.3145` n `8`; equity avg `-0.4776` n `102`; fx avg `-0.0098` n `6`; index avg `-0.0176` n `25`; metal avg `0.0359` n `20`; unknown avg `0.088` n `776`
- 4h: commodity avg `0.7523` n `12`; crypto_alt avg `-0.27` n `230`; crypto_major avg `-0.2899` n `8`; equity avg `-0.0544` n `102`; fx avg `-0.0163` n `6`; index avg `-0.036` n `25`; metal avg `-0.064` n `20`; unknown avg `0.3987` n `776`
- 24h: commodity avg `-0.2162` n `12`; crypto_alt avg `-0.3155` n `230`; crypto_major avg `-0.2585` n `8`; equity avg `-2.8574` n `102`; fx avg `-0.0984` n `6`; index avg `-0.3764` n `25`; metal avg `-0.4516` n `20`; unknown avg `0.3016` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
