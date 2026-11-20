# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T17:37:32.074049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.1229` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.0594` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.0371` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0748` n `13`; crypto_alt avg `0.1452` n `239`; crypto_major avg `-0.1235` n `8`; equity avg `0.1071` n `166`; fx avg `-0.0041` n `6`; index avg `0.0052` n `27`; metal avg `0.0259` n `20`; unknown avg `317.0443` n `1262`
- 1h: commodity avg `0.0115` n `13`; crypto_alt avg `-0.774` n `239`; crypto_major avg `-0.9735` n `8`; equity avg `-0.6618` n `166`; fx avg `0.024` n `6`; index avg `-0.0897` n `27`; metal avg `-0.1526` n `20`; unknown avg `0.2605` n `1255`
- 4h: commodity avg `-0.2026` n `13`; crypto_alt avg `-2.9747` n `239`; crypto_major avg `-3.3255` n `8`; equity avg `-2.7139` n `166`; fx avg `0.007` n `6`; index avg `-0.2661` n `27`; metal avg `-0.2884` n `20`; unknown avg `1.9134` n `1245`
- 24h: commodity avg `-0.3341` n `13`; crypto_alt avg `-6.5824` n `239`; crypto_major avg `-7.2719` n `8`; equity avg `-9.0362` n `166`; fx avg `0.0179` n `6`; index avg `-0.8267` n `27`; metal avg `-1.3462` n `20`; unknown avg `46.5042` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
