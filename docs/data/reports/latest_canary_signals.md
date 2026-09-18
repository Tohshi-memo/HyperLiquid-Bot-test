# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T03:52:33.875563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0345` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7682` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5008` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `0.303` n `234`; crypto_major avg `0.3626` n `8`; equity avg `0.0904` n `140`; fx avg `0.0138` n `6`; index avg `0.029` n `26`; metal avg `0.0522` n `20`; unknown avg `-0.2667` n `919`
- 1h: commodity avg `-0.0206` n `12`; crypto_alt avg `1.3187` n `234`; crypto_major avg `1.0439` n `8`; equity avg `0.4524` n `140`; fx avg `0.1496` n `6`; index avg `0.0946` n `26`; metal avg `0.0521` n `20`; unknown avg `29.1987` n `913`
- 4h: commodity avg `-0.0516` n `12`; crypto_alt avg `2.8593` n `234`; crypto_major avg `1.9829` n `8`; equity avg `0.4821` n `140`; fx avg `0.1886` n `6`; index avg `0.041` n `26`; metal avg `0.2147` n `20`; unknown avg `4.322` n `897`
- 24h: commodity avg `-0.3007` n `12`; crypto_alt avg `5.7296` n `234`; crypto_major avg `3.4917` n `8`; equity avg `1.9567` n `140`; fx avg `0.1831` n `6`; index avg `0.2831` n `26`; metal avg `0.482` n `20`; unknown avg `1.9771` n `753`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
