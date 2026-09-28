# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T23:37:24.917072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.0328` n `234`; crypto_major avg `0.0887` n `8`; equity avg `0.0208` n `141`; fx avg `-0.0083` n `6`; index avg `-0.003` n `26`; metal avg `0.0112` n `20`; unknown avg `-0.1145` n `963`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `0.7905` n `234`; crypto_major avg `0.2877` n `8`; equity avg `0.0544` n `141`; fx avg `-0.0333` n `6`; index avg `0.0021` n `26`; metal avg `0.0287` n `20`; unknown avg `0.227` n `961`
- 4h: commodity avg `0.0745` n `12`; crypto_alt avg `0.932` n `234`; crypto_major avg `0.3309` n `8`; equity avg `0.0029` n `141`; fx avg `-0.0291` n `6`; index avg `0.0085` n `26`; metal avg `-0.0704` n `20`; unknown avg `-0.1834` n `873`
- 24h: commodity avg `-0.0126` n `12`; crypto_alt avg `-3.1665` n `234`; crypto_major avg `-1.7156` n `8`; equity avg `-2.9026` n `141`; fx avg `0.0261` n `6`; index avg `-0.2189` n `26`; metal avg `-0.9143` n `20`; unknown avg `94.6921` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
