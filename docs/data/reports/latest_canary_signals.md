# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T19:07:34.366898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `13`; crypto_alt avg `-0.3117` n `238`; crypto_major avg `-0.2601` n `8`; equity avg `-0.0791` n `156`; fx avg `-0.0084` n `6`; index avg `0.0008` n `27`; metal avg `0.0117` n `20`; unknown avg `1.3776` n `1232`
- 1h: commodity avg `-0.0677` n `13`; crypto_alt avg `-0.6815` n `238`; crypto_major avg `-0.3287` n `8`; equity avg `-0.2392` n `156`; fx avg `-0.0126` n `6`; index avg `0.0024` n `27`; metal avg `0.0274` n `20`; unknown avg `0.3218` n `1232`
- 4h: commodity avg `0.3591` n `13`; crypto_alt avg `-0.9194` n `238`; crypto_major avg `-0.3544` n `8`; equity avg `-0.8366` n `156`; fx avg `0.0194` n `6`; index avg `-0.064` n `27`; metal avg `-0.0578` n `20`; unknown avg `38.0099` n `1228`
- 24h: commodity avg `-0.4806` n `13`; crypto_alt avg `-1.0514` n `238`; crypto_major avg `1.0432` n `8`; equity avg `-1.875` n `155`; fx avg `0.0214` n `6`; index avg `-0.1758` n `27`; metal avg `-0.513` n `20`; unknown avg `10.3889` n `946`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
