# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T20:52:24.977480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `0.2337` n `228`; crypto_major avg `0.1184` n `8`; equity avg `0.0391` n `67`; fx avg `-0.0003` n `6`; index avg `0.0126` n `23`; metal avg `0.0009` n `18`; unknown avg `0.0388` n `419`
- 1h: commodity avg `-0.0189` n `12`; crypto_alt avg `0.0927` n `228`; crypto_major avg `0.173` n `8`; equity avg `0.1846` n `67`; fx avg `0.0024` n `6`; index avg `0.1064` n `23`; metal avg `0.0125` n `18`; unknown avg `0.4252` n `419`
- 4h: commodity avg `-0.3147` n `12`; crypto_alt avg `-0.2804` n `228`; crypto_major avg `-0.1356` n `8`; equity avg `0.3469` n `67`; fx avg `0.0241` n `6`; index avg `0.1304` n `23`; metal avg `-0.0587` n `18`; unknown avg `0.0094` n `418`
- 24h: commodity avg `-1.1306` n `12`; crypto_alt avg `-0.2771` n `228`; crypto_major avg `0.0358` n `8`; equity avg `0.1036` n `67`; fx avg `-0.0769` n `6`; index avg `-0.3662` n `23`; metal avg `-1.2965` n `18`; unknown avg `-0.1007` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
