# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T02:52:16.206869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `-0.0709` n `228`; crypto_major avg `-0.1035` n `8`; equity avg `0.0003` n `65`; fx avg `0.0023` n `5`; index avg `-0.0154` n `23`; metal avg `0.0266` n `18`; unknown avg `-0.0863` n `375`
- 1h: commodity avg `0.1137` n `12`; crypto_alt avg `-0.1185` n `228`; crypto_major avg `-0.1001` n `8`; equity avg `0.0377` n `65`; fx avg `-0.0189` n `5`; index avg `0.1243` n `23`; metal avg `0.1369` n `18`; unknown avg `0.211` n `375`
- 4h: commodity avg `0.0369` n `12`; crypto_alt avg `0.9419` n `228`; crypto_major avg `0.6433` n `8`; equity avg `0.1354` n `65`; fx avg `-0.0127` n `5`; index avg `0.1832` n `23`; metal avg `0.2432` n `18`; unknown avg `0.2622` n `375`
- 24h: commodity avg `-0.1966` n `12`; crypto_alt avg `4.7363` n `228`; crypto_major avg `2.7119` n `8`; equity avg `3.9115` n `65`; fx avg `0.0946` n `5`; index avg `1.4435` n `23`; metal avg `0.4439` n `18`; unknown avg `1.7314` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
