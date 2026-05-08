# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T23:07:11.053179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.018` n `12`; crypto_alt avg `-0.2043` n `228`; crypto_major avg `-0.1426` n `8`; equity avg `-0.0477` n `65`; fx avg `0.0008` n `5`; index avg `0.0477` n `23`; metal avg `-0.0215` n `18`; unknown avg `-0.1565` n `375`
- 1h: commodity avg `-0.119` n `12`; crypto_alt avg `-0.2085` n `228`; crypto_major avg `-0.2176` n `8`; equity avg `-0.0023` n `65`; fx avg `-0.0074` n `5`; index avg `0.0791` n `23`; metal avg `-0.1755` n `18`; unknown avg `-0.2309` n `375`
- 4h: commodity avg `-0.3263` n `12`; crypto_alt avg `0.3968` n `228`; crypto_major avg `-0.0137` n `8`; equity avg `0.69` n `65`; fx avg `-0.0069` n `5`; index avg `0.1768` n `23`; metal avg `-0.3029` n `18`; unknown avg `-0.6469` n `375`
- 24h: commodity avg `-0.7976` n `12`; crypto_alt avg `3.6125` n `228`; crypto_major avg `1.6276` n `8`; equity avg `4.2139` n `65`; fx avg `0.2191` n `5`; index avg `1.6662` n `23`; metal avg `0.9953` n `18`; unknown avg `0.8031` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
