# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T09:07:34.000413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5483` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4832` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.5875` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5722` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `0.0504` n `234`; crypto_major avg `-0.075` n `8`; equity avg `0.0945` n `140`; fx avg `0.0017` n `6`; index avg `0.0061` n `26`; metal avg `0.0164` n `20`; unknown avg `9.1586` n `942`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `1.2593` n `234`; crypto_major avg `1.6622` n `8`; equity avg `0.4215` n `140`; fx avg `-0.0247` n `6`; index avg `0.0367` n `26`; metal avg `0.0747` n `20`; unknown avg `5.3539` n `942`
- 4h: commodity avg `-0.0154` n `12`; crypto_alt avg `1.7762` n `234`; crypto_major avg `2.5329` n `8`; equity avg `0.9607` n `140`; fx avg `-0.1005` n `6`; index avg `0.1417` n `26`; metal avg `0.0497` n `20`; unknown avg `9.9183` n `890`
- 24h: commodity avg `-0.5746` n `12`; crypto_alt avg `5.9335` n `234`; crypto_major avg `5.2628` n `8`; equity avg `2.0336` n `140`; fx avg `-0.1082` n `6`; index avg `0.3633` n `26`; metal avg `0.0431` n `20`; unknown avg `3.865` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
