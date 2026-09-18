# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T15:07:30.862223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.1379` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `3.0471` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.4957` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0421` n `12`; crypto_alt avg `-0.2354` n `234`; crypto_major avg `-0.3563` n `8`; equity avg `-0.0967` n `140`; fx avg `0.0105` n `6`; index avg `-0.0049` n `26`; metal avg `-0.0217` n `20`; unknown avg `0.0207` n `926`
- 1h: commodity avg `-0.0734` n `12`; crypto_alt avg `0.4194` n `234`; crypto_major avg `0.7617` n `8`; equity avg `0.3614` n `140`; fx avg `-0.0395` n `6`; index avg `0.016` n `26`; metal avg `0.0644` n `20`; unknown avg `-0.3109` n `924`
- 4h: commodity avg `0.3081` n `12`; crypto_alt avg `1.5599` n `234`; crypto_major avg `2.8038` n `8`; equity avg `-0.3341` n `140`; fx avg `-0.0532` n `6`; index avg `-0.1286` n `26`; metal avg `-0.2433` n `20`; unknown avg `2.1483` n `893`
- 24h: commodity avg `0.148` n `12`; crypto_alt avg `6.4861` n `234`; crypto_major avg `6.5773` n `8`; equity avg `0.7859` n `140`; fx avg `0.2101` n `6`; index avg `-0.0604` n `26`; metal avg `0.1597` n `20`; unknown avg `3.9809` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
