# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T03:07:34.847533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3504` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3255` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2512` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.1052` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.0964` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.0526` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.366` n `230`; crypto_major avg `0.2639` n `8`; equity avg `0.0018` n `121`; fx avg `0.0029` n `6`; index avg `0.0035` n `25`; metal avg `0.0074` n `20`; unknown avg `0.0806` n `793`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `1.8535` n `230`; crypto_major avg `2.1046` n `8`; equity avg `0.052` n `121`; fx avg `0.0149` n `6`; index avg `0.0029` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.0095` n `793`
- 4h: commodity avg `-0.05` n `12`; crypto_alt avg `2.9947` n `230`; crypto_major avg `2.3004` n `8`; equity avg `0.0492` n `121`; fx avg `0.0255` n `6`; index avg `0.0054` n `25`; metal avg `-0.0251` n `20`; unknown avg `0.0819` n `793`
- 24h: commodity avg `0.0568` n `12`; crypto_alt avg `11.2054` n `230`; crypto_major avg `9.7701` n `8`; equity avg `0.2714` n `121`; fx avg `0.0601` n `6`; index avg `-0.0038` n `25`; metal avg `0.2161` n `20`; unknown avg `1.5171` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
