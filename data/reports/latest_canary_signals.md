# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T11:52:29.864309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.072` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6658` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2471` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0403` n `12`; crypto_alt avg `-0.0183` n `234`; crypto_major avg `0.0232` n `8`; equity avg `0.13` n `140`; fx avg `0.0063` n `6`; index avg `0.018` n `26`; metal avg `0.0836` n `20`; unknown avg `1.1023` n `920`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `0.3034` n `234`; crypto_major avg `0.581` n `8`; equity avg `-0.0145` n `140`; fx avg `0.0194` n `6`; index avg `0.0089` n `26`; metal avg `0.1952` n `20`; unknown avg `14.0276` n `916`
- 4h: commodity avg `-0.2042` n `12`; crypto_alt avg `2.2895` n `234`; crypto_major avg `2.8678` n `8`; equity avg `0.6207` n `140`; fx avg `-0.0083` n `6`; index avg `0.0938` n `26`; metal avg `0.202` n `20`; unknown avg `11.5576` n `910`
- 24h: commodity avg `-0.8038` n `12`; crypto_alt avg `6.8563` n `234`; crypto_major avg `5.7711` n `8`; equity avg `2.0253` n `140`; fx avg `-0.0833` n `6`; index avg `0.3765` n `26`; metal avg `0.1821` n `20`; unknown avg `6.7276` n `733`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
