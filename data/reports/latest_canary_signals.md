# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T21:44:01.958236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0615` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0265` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9897` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.7166` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.6861` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `0.4368` n `230`; crypto_major avg `0.7751` n `8`; equity avg `0.0143` n `121`; fx avg `-0.001` n `6`; index avg `0.0059` n `25`; metal avg `0.0327` n `20`; unknown avg `0.0885` n `793`
- 1h: commodity avg `-0.0073` n `12`; crypto_alt avg `1.169` n `230`; crypto_major avg `1.7111` n `8`; equity avg `-0.0055` n `121`; fx avg `0.0144` n `6`; index avg `0.0027` n `25`; metal avg `0.025` n `20`; unknown avg `-0.0648` n `793`
- 4h: commodity avg `-0.1086` n `12`; crypto_alt avg `1.1938` n `230`; crypto_major avg `1.9529` n `8`; equity avg `-0.0368` n `121`; fx avg `0.0099` n `6`; index avg `-0.0175` n `25`; metal avg `-0.0736` n `20`; unknown avg `-0.2384` n `793`
- 24h: commodity avg `0.1611` n `12`; crypto_alt avg `8.1726` n `230`; crypto_major avg `6.4121` n `8`; equity avg `0.8714` n `121`; fx avg `-0.0648` n `6`; index avg `0.1005` n `25`; metal avg `0.5341` n `20`; unknown avg `1.2473` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
