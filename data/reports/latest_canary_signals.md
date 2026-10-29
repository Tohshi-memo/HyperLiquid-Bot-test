# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T17:37:30.539322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1485` n `13`; crypto_alt avg `-0.1134` n `238`; crypto_major avg `-0.0677` n `8`; equity avg `-0.0528` n `156`; fx avg `0.0063` n `6`; index avg `-0.0037` n `27`; metal avg `-0.0363` n `20`; unknown avg `4.869` n `1238`
- 1h: commodity avg `0.1587` n `13`; crypto_alt avg `-0.3879` n `238`; crypto_major avg `-0.3748` n `8`; equity avg `-0.3649` n `156`; fx avg `0.0126` n `6`; index avg `-0.0286` n `27`; metal avg `0.0004` n `20`; unknown avg `8.3619` n `1232`
- 4h: commodity avg `0.362` n `13`; crypto_alt avg `1.4147` n `238`; crypto_major avg `1.3436` n `8`; equity avg `0.4055` n `156`; fx avg `0.162` n `6`; index avg `0.0644` n `27`; metal avg `0.0218` n `20`; unknown avg `0.6113` n `1132`
- 24h: commodity avg `-0.5249` n `13`; crypto_alt avg `1.2394` n `238`; crypto_major avg `2.5377` n `8`; equity avg `-0.7525` n `155`; fx avg `0.0369` n `6`; index avg `-0.1468` n `27`; metal avg `-0.4598` n `20`; unknown avg `9.4276` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
