# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T03:52:27.752938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `0.0055` n `230`; crypto_major avg `-0.0013` n `8`; equity avg `0.0092` n `114`; fx avg `0.0005` n `6`; index avg `0.0016` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0088` n `791`
- 1h: commodity avg `0.0413` n `12`; crypto_alt avg `0.1991` n `230`; crypto_major avg `0.0351` n `8`; equity avg `0.0908` n `114`; fx avg `-0.0004` n `6`; index avg `0.0026` n `25`; metal avg `0.007` n `20`; unknown avg `0.0889` n `791`
- 4h: commodity avg `0.0433` n `12`; crypto_alt avg `-0.1028` n `230`; crypto_major avg `0.0962` n `8`; equity avg `0.1435` n `114`; fx avg `-0.0015` n `6`; index avg `0.0078` n `25`; metal avg `0.018` n `20`; unknown avg `-0.0439` n `791`
- 24h: commodity avg `-0.0401` n `12`; crypto_alt avg `0.1264` n `230`; crypto_major avg `-0.0679` n `8`; equity avg `0.2591` n `114`; fx avg `-0.0251` n `6`; index avg `0.0179` n `25`; metal avg `0.0114` n `20`; unknown avg `-0.0488` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2216`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
