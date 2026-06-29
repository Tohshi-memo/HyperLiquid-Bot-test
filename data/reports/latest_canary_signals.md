# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T10:37:31.691056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `-0.1155` n `228`; crypto_major avg `-0.0556` n `8`; equity avg `0.0897` n `88`; fx avg `0.0049` n `6`; index avg `0.0159` n `23`; metal avg `-0.0068` n `20`; unknown avg `0.0034` n `764`
- 1h: commodity avg `-0.0911` n `12`; crypto_alt avg `0.228` n `228`; crypto_major avg `0.5712` n `8`; equity avg `0.1659` n `88`; fx avg `0.0235` n `6`; index avg `0.025` n `23`; metal avg `-0.1216` n `20`; unknown avg `0.2086` n `764`
- 4h: commodity avg `-0.1985` n `12`; crypto_alt avg `0.0763` n `228`; crypto_major avg `0.3666` n `8`; equity avg `0.2696` n `88`; fx avg `0.0112` n `6`; index avg `0.0401` n `23`; metal avg `-0.3815` n `20`; unknown avg `0.0407` n `764`
- 24h: commodity avg `-0.4043` n `12`; crypto_alt avg `0.5654` n `228`; crypto_major avg `0.6605` n `8`; equity avg `0.6222` n `88`; fx avg `0.0666` n `6`; index avg `0.1018` n `23`; metal avg `-0.5048` n `20`; unknown avg `0.4332` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
