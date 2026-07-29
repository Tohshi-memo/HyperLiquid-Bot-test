# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T00:22:37.619636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0733` n `12`; crypto_alt avg `-0.02` n `230`; crypto_major avg `-0.0414` n `8`; equity avg `0.1035` n `102`; fx avg `-0.0045` n `6`; index avg `0.0142` n `25`; metal avg `-0.0061` n `20`; unknown avg `0.0602` n `777`
- 1h: commodity avg `-0.1681` n `12`; crypto_alt avg `0.6456` n `230`; crypto_major avg `0.8146` n `8`; equity avg `1.8766` n `102`; fx avg `0.0355` n `6`; index avg `0.2792` n `25`; metal avg `0.0873` n `20`; unknown avg `0.4361` n `776`
- 4h: commodity avg `0.5441` n `12`; crypto_alt avg `0.1185` n `230`; crypto_major avg `0.1088` n `8`; equity avg `1.1546` n `102`; fx avg `0.0241` n `6`; index avg `0.2527` n `25`; metal avg `0.0212` n `20`; unknown avg `-0.0263` n `776`
- 24h: commodity avg `-0.2586` n `12`; crypto_alt avg `0.1847` n `230`; crypto_major avg `0.503` n `8`; equity avg `-0.7889` n `102`; fx avg `-0.1335` n `6`; index avg `0.0393` n `25`; metal avg `-0.2702` n `20`; unknown avg `0.4177` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
