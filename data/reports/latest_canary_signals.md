# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T02:07:20.232866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `-0.1297` n `228`; crypto_major avg `-0.0137` n `8`; equity avg `0.0018` n `65`; fx avg `0.0` n `5`; index avg `0.0842` n `23`; metal avg `0.0342` n `18`; unknown avg `0.2069` n `375`
- 1h: commodity avg `0.1264` n `12`; crypto_alt avg `0.4417` n `228`; crypto_major avg `0.5708` n `8`; equity avg `0.0396` n `65`; fx avg `0.0204` n `5`; index avg `0.1044` n `23`; metal avg `0.0815` n `18`; unknown avg `0.5683` n `375`
- 4h: commodity avg `-0.2085` n `12`; crypto_alt avg `0.9266` n `228`; crypto_major avg `0.6549` n `8`; equity avg `0.1446` n `65`; fx avg `-0.0021` n `5`; index avg `0.1747` n `23`; metal avg `-0.0155` n `18`; unknown avg `0.1691` n `375`
- 24h: commodity avg `-0.5176` n `12`; crypto_alt avg `5.2426` n `228`; crypto_major avg `3.0031` n `8`; equity avg `3.8088` n `65`; fx avg `0.1074` n `5`; index avg `1.3654` n `23`; metal avg `0.1098` n `18`; unknown avg `2.4227` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
