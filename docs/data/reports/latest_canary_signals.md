# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T01:25:47.779825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0923` n `12`; crypto_alt avg `0.1774` n `228`; crypto_major avg `0.1255` n `8`; equity avg `0.0411` n `65`; fx avg `0.0` n `5`; index avg `-0.0063` n `23`; metal avg `0.0189` n `18`; unknown avg `0.2338` n `375`
- 1h: commodity avg `-0.0093` n `12`; crypto_alt avg `0.573` n `228`; crypto_major avg `0.2854` n `8`; equity avg `0.11` n `65`; fx avg `-0.0072` n `5`; index avg `0.0406` n `23`; metal avg `0.1506` n `18`; unknown avg `0.208` n `375`
- 4h: commodity avg `-0.2983` n `12`; crypto_alt avg `1.2375` n `228`; crypto_major avg `0.5248` n `8`; equity avg `0.3093` n `65`; fx avg `-0.0268` n `5`; index avg `0.159` n `23`; metal avg `-0.1053` n `18`; unknown avg `0.0524` n `375`
- 24h: commodity avg `-0.4926` n `12`; crypto_alt avg `4.5443` n `228`; crypto_major avg `2.2813` n `8`; equity avg `3.6284` n `65`; fx avg `0.1073` n `5`; index avg `1.2797` n `23`; metal avg `0.205` n `18`; unknown avg `1.4082` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
