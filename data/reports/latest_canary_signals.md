# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T22:52:21.649411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.5845` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `2.4747` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.3484` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1925` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.1757` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.8621` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.7901` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.718` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0992` n `12`; crypto_alt avg `-1.4341` n `228`; crypto_major avg `-1.251` n `8`; equity avg `-0.2894` n `69`; fx avg `-0.003` n `6`; index avg `-0.043` n `23`; metal avg `-0.0564` n `18`; unknown avg `0.5328` n `422`
- 1h: commodity avg `0.284` n `12`; crypto_alt avg `-2.0301` n `228`; crypto_major avg `-1.8917` n `8`; equity avg `-0.1737` n `69`; fx avg `-0.0114` n `6`; index avg `-0.0296` n `23`; metal avg `-0.1016` n `18`; unknown avg `-0.644` n `422`
- 4h: commodity avg `0.101` n `12`; crypto_alt avg `-1.6954` n `228`; crypto_major avg `-2.2474` n `8`; equity avg `0.3371` n `69`; fx avg `-0.0212` n `6`; index avg `0.2273` n `23`; metal avg `-0.0549` n `18`; unknown avg `-0.2725` n `422`
- 24h: commodity avg `0.0121` n `12`; crypto_alt avg `-5.3821` n `228`; crypto_major avg `-6.9168` n `8`; equity avg `1.1531` n `69`; fx avg `0.0679` n `6`; index avg `0.7671` n `23`; metal avg `0.3135` n `18`; unknown avg `-0.6382` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
