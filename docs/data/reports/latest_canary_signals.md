# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T00:52:19.985562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2399` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5431` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5996` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `0.2192` n `228`; crypto_major avg `0.0548` n `8`; equity avg `-0.3371` n `74`; fx avg `-0.0288` n `6`; index avg `-0.2604` n `23`; metal avg `-0.1645` n `18`; unknown avg `-0.0213` n `517`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `1.1519` n `228`; crypto_major avg `1.2013` n `8`; equity avg `1.0608` n `74`; fx avg `-0.0312` n `6`; index avg `0.3344` n `23`; metal avg `0.0973` n `18`; unknown avg `-0.1007` n `517`
- 4h: commodity avg `-0.1836` n `12`; crypto_alt avg `2.5658` n `228`; crypto_major avg `3.0563` n `8`; equity avg `1.4567` n `74`; fx avg `-0.044` n `6`; index avg `0.4476` n `23`; metal avg `0.5132` n `18`; unknown avg `0.7171` n `516`
- 24h: commodity avg `-0.0183` n `12`; crypto_alt avg `3.7121` n `228`; crypto_major avg `5.9602` n `8`; equity avg `2.3161` n `74`; fx avg `-0.0904` n `6`; index avg `0.6915` n `23`; metal avg `0.7373` n `18`; unknown avg `-4.4683` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
