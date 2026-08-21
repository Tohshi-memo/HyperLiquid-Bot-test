# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T23:43:27.734466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.5013` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.4355` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.4072` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.3941` n `230`; crypto_major avg `-0.7969` n `8`; equity avg `0.0164` n `121`; fx avg `-0.0001` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0073` n `20`; unknown avg `0.0641` n `793`
- 1h: commodity avg `0.0` n `12`; crypto_alt avg `-0.0898` n `230`; crypto_major avg `-0.2306` n `8`; equity avg `-0.0131` n `121`; fx avg `-0.0061` n `6`; index avg `0.0082` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.2619` n `793`
- 4h: commodity avg `0.0475` n `12`; crypto_alt avg `2.8111` n `230`; crypto_major avg `3.483` n `8`; equity avg `0.0758` n `121`; fx avg `-0.0076` n `6`; index avg `0.0175` n `25`; metal avg `-0.0183` n `20`; unknown avg `-0.0787` n `793`
- 24h: commodity avg `0.1652` n `12`; crypto_alt avg `8.2434` n `230`; crypto_major avg `7.35` n `8`; equity avg `0.9797` n `121`; fx avg `-0.1019` n `6`; index avg `0.1424` n `25`; metal avg `0.4485` n `20`; unknown avg `1.381` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
