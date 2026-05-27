# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T20:22:24.818221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `0.0666` n `228`; crypto_major avg `0.0717` n `8`; equity avg `0.0659` n `67`; fx avg `0.0017` n `6`; index avg `0.0877` n `23`; metal avg `0.0723` n `18`; unknown avg `0.1718` n `419`
- 1h: commodity avg `0.0878` n `12`; crypto_alt avg `0.0151` n `228`; crypto_major avg `0.3159` n `8`; equity avg `0.1781` n `67`; fx avg `0.0043` n `6`; index avg `0.0555` n `23`; metal avg `0.0718` n `18`; unknown avg `0.1031` n `419`
- 4h: commodity avg `-0.4605` n `12`; crypto_alt avg `-0.3034` n `228`; crypto_major avg `0.0891` n `8`; equity avg `0.3693` n `67`; fx avg `0.0238` n `6`; index avg `0.1803` n `23`; metal avg `0.1223` n `18`; unknown avg `-0.0388` n `418`
- 24h: commodity avg `-1.2034` n `12`; crypto_alt avg `-0.3044` n `228`; crypto_major avg `0.026` n `8`; equity avg `0.0168` n `67`; fx avg `-0.0806` n `6`; index avg `-0.421` n `23`; metal avg `-1.2577` n `18`; unknown avg `-0.0695` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
