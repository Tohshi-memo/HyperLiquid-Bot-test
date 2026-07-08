# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T06:52:33.556067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `0.222` n `229`; crypto_major avg `0.2467` n `8`; equity avg `-0.0322` n `91`; fx avg `-0.0029` n `6`; index avg `0.01` n `25`; metal avg `-0.0334` n `20`; unknown avg `0.0277` n `763`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0234` n `229`; crypto_major avg `-0.0543` n `8`; equity avg `-0.116` n `91`; fx avg `-0.0573` n `6`; index avg `-0.0232` n `25`; metal avg `0.0136` n `20`; unknown avg `-0.1712` n `745`
- 4h: commodity avg `0.1009` n `12`; crypto_alt avg `-0.1912` n `229`; crypto_major avg `-0.505` n `8`; equity avg `-0.4232` n `91`; fx avg `-0.0928` n `6`; index avg `-0.2028` n `25`; metal avg `0.2058` n `20`; unknown avg `-0.2519` n `743`
- 24h: commodity avg `0.8313` n `12`; crypto_alt avg `-2.9265` n `229`; crypto_major avg `-2.5685` n `8`; equity avg `-1.8799` n `91`; fx avg `-0.3049` n `6`; index avg `-0.3791` n `25`; metal avg `0.0268` n `20`; unknown avg `-0.6413` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
