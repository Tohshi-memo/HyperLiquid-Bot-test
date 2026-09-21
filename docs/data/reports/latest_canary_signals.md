# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T08:52:26.795231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.3836` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3677` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.1181` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.0635` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6394` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.6203` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0431` n `12`; crypto_alt avg `0.5167` n `234`; crypto_major avg `0.8148` n `8`; equity avg `0.088` n `140`; fx avg `0.0034` n `6`; index avg `0.0075` n `26`; metal avg `-0.0057` n `20`; unknown avg `1.1635` n `944`
- 1h: commodity avg `0.0059` n `12`; crypto_alt avg `1.2744` n `234`; crypto_major avg `2.124` n `8`; equity avg `0.5037` n `140`; fx avg `-0.0459` n `6`; index avg `0.0609` n `26`; metal avg `0.0605` n `20`; unknown avg `8.9172` n `936`
- 4h: commodity avg `0.0064` n `12`; crypto_alt avg `1.345` n `234`; crypto_major avg `2.3741` n `8`; equity avg `0.7347` n `140`; fx avg `-0.1073` n `6`; index avg `0.1195` n `26`; metal avg `-0.0095` n `20`; unknown avg `5.8681` n `890`
- 24h: commodity avg `-0.626` n `12`; crypto_alt avg `6.0096` n `234`; crypto_major avg `5.4542` n `8`; equity avg `1.9471` n `140`; fx avg `-0.11` n `6`; index avg `0.3582` n `26`; metal avg `0.0394` n `20`; unknown avg `5.8295` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
