# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T03:04:48.791695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2797` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.262` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1471` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.0363` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.0348` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.9505` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.3436` n `230`; crypto_major avg `0.1995` n `8`; equity avg `0.0378` n `121`; fx avg `0.0071` n `6`; index avg `0.0018` n `25`; metal avg `0.003` n `20`; unknown avg `0.1138` n `793`
- 1h: commodity avg `0.0022` n `12`; crypto_alt avg `1.8297` n `230`; crypto_major avg `2.0385` n `8`; equity avg `0.088` n `121`; fx avg `0.0191` n `6`; index avg `0.0011` n `25`; metal avg `0.0037` n `20`; unknown avg `0.1044` n `793`
- 4h: commodity avg `-0.0473` n `12`; crypto_alt avg `2.9722` n `230`; crypto_major avg `2.2324` n `8`; equity avg `0.0853` n `121`; fx avg `0.0297` n `6`; index avg `0.0037` n `25`; metal avg `-0.0296` n `20`; unknown avg `0.2761` n `793`
- 24h: commodity avg `0.0595` n `12`; crypto_alt avg `11.181` n `230`; crypto_major avg `9.6912` n `8`; equity avg `0.3066` n `121`; fx avg `0.0643` n `6`; index avg `-0.0055` n `25`; metal avg `0.2116` n `20`; unknown avg `1.4785` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
