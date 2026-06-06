# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T20:52:25.109983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1003` n `12`; crypto_alt avg `-0.0555` n `228`; crypto_major avg `0.032` n `8`; equity avg `-0.0024` n `74`; fx avg `-0.0016` n `6`; index avg `0.0844` n `23`; metal avg `-0.005` n `18`; unknown avg `0.0109` n `515`
- 1h: commodity avg `-0.0296` n `12`; crypto_alt avg `-0.0283` n `228`; crypto_major avg `0.2139` n `8`; equity avg `0.1387` n `74`; fx avg `-0.0014` n `6`; index avg `0.1399` n `23`; metal avg `-0.013` n `18`; unknown avg `-0.1337` n `515`
- 4h: commodity avg `0.1758` n `12`; crypto_alt avg `-0.6822` n `228`; crypto_major avg `-0.7429` n `8`; equity avg `0.0937` n `74`; fx avg `0.0063` n `6`; index avg `0.0145` n `23`; metal avg `0.0215` n `18`; unknown avg `0.4946` n `515`
- 24h: commodity avg `0.6606` n `12`; crypto_alt avg `-2.6165` n `228`; crypto_major avg `-2.3608` n `8`; equity avg `-0.69` n `74`; fx avg `0.0535` n `6`; index avg `0.2849` n `23`; metal avg `-0.5204` n `18`; unknown avg `-0.634` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
