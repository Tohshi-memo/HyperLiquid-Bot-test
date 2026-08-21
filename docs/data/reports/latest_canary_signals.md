# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T22:22:25.076728+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.9463` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.9437` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.7888` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.9267` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.893` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `-0.033` n `230`; crypto_major avg `-0.2535` n `8`; equity avg `-0.0` n `121`; fx avg `0.0022` n `6`; index avg `-0.004` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.2833` n `793`
- 1h: commodity avg `0.0129` n `12`; crypto_alt avg `1.168` n `230`; crypto_major avg `1.9419` n `8`; equity avg `0.0489` n `121`; fx avg `-0.0072` n `6`; index avg `0.0144` n `25`; metal avg `0.0152` n `20`; unknown avg `1.1246` n `793`
- 4h: commodity avg `-0.0619` n `12`; crypto_alt avg `1.534` n `230`; crypto_major avg `2.8818` n `8`; equity avg `0.093` n `121`; fx avg `-0.0031` n `6`; index avg `0.0057` n `25`; metal avg `-0.0645` n `20`; unknown avg `0.9924` n `793`
- 24h: commodity avg `0.1819` n `12`; crypto_alt avg `8.8646` n `230`; crypto_major avg `8.1113` n `8`; equity avg `1.0319` n `121`; fx avg `-0.0598` n `6`; index avg `0.1264` n `25`; metal avg `0.5178` n `20`; unknown avg `2.5275` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
