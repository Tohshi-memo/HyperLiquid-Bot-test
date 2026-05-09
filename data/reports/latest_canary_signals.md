# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T04:55:35.060422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.1545` n `228`; crypto_major avg `-0.1039` n `8`; equity avg `0.0015` n `65`; fx avg `-0.0006` n `5`; index avg `-0.0042` n `23`; metal avg `-0.017` n `18`; unknown avg `-0.0496` n `375`
- 1h: commodity avg `0.0913` n `12`; crypto_alt avg `0.1463` n `228`; crypto_major avg `0.0187` n `8`; equity avg `-0.0193` n `65`; fx avg `-0.0006` n `5`; index avg `0.0396` n `23`; metal avg `-0.0468` n `18`; unknown avg `0.1463` n `375`
- 4h: commodity avg `0.1503` n `12`; crypto_alt avg `0.4474` n `228`; crypto_major avg `0.5958` n `8`; equity avg `0.0758` n `65`; fx avg `-0.0043` n `5`; index avg `0.2631` n `23`; metal avg `0.1632` n `18`; unknown avg `-0.1006` n `375`
- 24h: commodity avg `-0.2577` n `12`; crypto_alt avg `4.3909` n `228`; crypto_major avg `2.8044` n `8`; equity avg `3.5813` n `65`; fx avg `0.0273` n `5`; index avg `1.4159` n `23`; metal avg `0.2651` n `18`; unknown avg `1.3571` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
