# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T09:37:31.849426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1221` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.1114` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1705` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.7073` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `0.5156` n `234`; crypto_major avg `0.8932` n `8`; equity avg `0.0737` n `140`; fx avg `0.0063` n `6`; index avg `0.0033` n `26`; metal avg `-0.0577` n `20`; unknown avg `6.1461` n `944`
- 1h: commodity avg `0.0722` n `12`; crypto_alt avg `1.3508` n `234`; crypto_major avg `1.6666` n `8`; equity avg `0.2212` n `140`; fx avg `0.0276` n `6`; index avg `0.0124` n `26`; metal avg `-0.0407` n `20`; unknown avg `9.712` n `942`
- 4h: commodity avg `0.0016` n `12`; crypto_alt avg `2.3804` n `234`; crypto_major avg `3.1237` n `8`; equity avg `0.9532` n `140`; fx avg `-0.0747` n `6`; index avg `0.1266` n `26`; metal avg `0.0123` n `20`; unknown avg `10.8521` n `890`
- 24h: commodity avg `-0.5479` n `12`; crypto_alt avg `6.3378` n `234`; crypto_major avg `5.8621` n `8`; equity avg `2.0382` n `140`; fx avg `-0.0848` n `6`; index avg `0.365` n `26`; metal avg `-0.0234` n `20`; unknown avg `3.241` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
