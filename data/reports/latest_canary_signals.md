# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T03:22:24.901980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8124` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.7903` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.6819` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.1753` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.1678` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.142` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `0.596` n `230`; crypto_major avg `0.8586` n `8`; equity avg `0.0006` n `121`; fx avg `-0.0014` n `6`; index avg `0.0052` n `25`; metal avg `0.0063` n `20`; unknown avg `0.5137` n `793`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `1.7207` n `230`; crypto_major avg `2.1733` n `8`; equity avg `0.0313` n `121`; fx avg `0.0083` n `6`; index avg `0.0105` n `25`; metal avg `0.0055` n `20`; unknown avg `0.1596` n `793`
- 4h: commodity avg `-0.045` n `12`; crypto_alt avg `3.3361` n `230`; crypto_major avg `2.7674` n `8`; equity avg `0.0855` n `121`; fx avg `0.024` n `6`; index avg `0.0085` n `25`; metal avg `-0.0229` n `20`; unknown avg `0.5235` n `793`
- 24h: commodity avg `0.0915` n `12`; crypto_alt avg `11.6915` n `230`; crypto_major avg `10.3842` n `8`; equity avg `0.2694` n `121`; fx avg `0.0498` n `6`; index avg `-0.0021` n `25`; metal avg `0.2344` n `20`; unknown avg `1.6048` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
