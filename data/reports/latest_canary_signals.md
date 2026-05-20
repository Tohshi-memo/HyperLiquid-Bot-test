# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T17:52:18.007091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8829` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1278` n `12`; crypto_alt avg `-0.1842` n `228`; crypto_major avg `-0.1387` n `8`; equity avg `-0.0432` n `66`; fx avg `0.0013` n `6`; index avg `-0.0686` n `23`; metal avg `-0.0498` n `18`; unknown avg `0.154` n `384`
- 1h: commodity avg `-0.0817` n `12`; crypto_alt avg `0.2536` n `228`; crypto_major avg `0.2378` n `8`; equity avg `0.157` n `66`; fx avg `0.0019` n `6`; index avg `0.0131` n `23`; metal avg `0.0997` n `18`; unknown avg `0.2915` n `384`
- 4h: commodity avg `-1.8807` n `12`; crypto_alt avg `1.7536` n `228`; crypto_major avg `1.0022` n `8`; equity avg `1.0186` n `66`; fx avg `0.0052` n `6`; index avg `0.5032` n `23`; metal avg `1.0635` n `18`; unknown avg `0.8982` n `384`
- 24h: commodity avg `-2.4294` n `12`; crypto_alt avg `2.6003` n `228`; crypto_major avg `1.7819` n `8`; equity avg `1.1218` n `66`; fx avg `-0.0207` n `6`; index avg `0.7688` n `23`; metal avg `1.0905` n `18`; unknown avg `1.4167` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0398`, n `668`, weak_sample_signal
