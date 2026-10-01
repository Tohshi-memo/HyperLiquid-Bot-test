# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T17:22:30.639222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0793` n `13`; crypto_alt avg `0.5694` n `234`; crypto_major avg `0.4462` n `8`; equity avg `0.4219` n `142`; fx avg `-0.0048` n `6`; index avg `0.0796` n `26`; metal avg `0.0709` n `20`; unknown avg `0.6527` n `975`
- 1h: commodity avg `0.0795` n `13`; crypto_alt avg `0.5826` n `234`; crypto_major avg `0.6127` n `8`; equity avg `0.6711` n `142`; fx avg `-0.0493` n `6`; index avg `0.1223` n `26`; metal avg `0.0976` n `20`; unknown avg `0.7937` n `973`
- 4h: commodity avg `0.0513` n `13`; crypto_alt avg `0.5092` n `234`; crypto_major avg `0.5173` n `8`; equity avg `0.4005` n `142`; fx avg `-0.1681` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0583` n `20`; unknown avg `2.3671` n `909`
- 24h: commodity avg `-0.2454` n `13`; crypto_alt avg `-1.0957` n `234`; crypto_major avg `-0.3457` n `8`; equity avg `0.7587` n `142`; fx avg `-0.1284` n `6`; index avg `0.0797` n `26`; metal avg `0.0184` n `20`; unknown avg `-0.0388` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
