# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T04:52:17.189763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.0968` n `228`; crypto_major avg `-0.0068` n `8`; equity avg `0.0282` n `65`; fx avg `0.0` n `5`; index avg `-0.0076` n `23`; metal avg `-0.0178` n `18`; unknown avg `0.0687` n `375`
- 1h: commodity avg `0.0964` n `12`; crypto_alt avg `0.2045` n `228`; crypto_major avg `0.1161` n `8`; equity avg `0.0072` n `65`; fx avg `0.0` n `5`; index avg `0.0362` n `23`; metal avg `-0.0477` n `18`; unknown avg `0.2244` n `375`
- 4h: commodity avg `0.1553` n `12`; crypto_alt avg `0.506` n `228`; crypto_major avg `0.6939` n `8`; equity avg `0.1009` n `65`; fx avg `-0.0036` n `5`; index avg `0.2597` n `23`; metal avg `0.1624` n `18`; unknown avg `-0.1033` n `375`
- 24h: commodity avg `-0.2526` n `12`; crypto_alt avg `4.4529` n `228`; crypto_major avg `2.9052` n `8`; equity avg `3.6044` n `65`; fx avg `0.028` n `5`; index avg `1.4124` n `23`; metal avg `0.2642` n `18`; unknown avg `1.388` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
