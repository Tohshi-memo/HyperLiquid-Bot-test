# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T14:37:31.519735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7831` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2201` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1425` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0778` n `12`; crypto_alt avg `0.1217` n `232`; crypto_major avg `0.5114` n `8`; equity avg `-0.1274` n `133`; fx avg `0.0039` n `6`; index avg `-0.0503` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.0238` n `792`
- 1h: commodity avg `0.0488` n `12`; crypto_alt avg `0.5406` n `232`; crypto_major avg `1.1871` n `8`; equity avg `0.2286` n `133`; fx avg `-0.0067` n `6`; index avg `-0.0073` n `26`; metal avg `0.0363` n `20`; unknown avg `17.1889` n `790`
- 4h: commodity avg `-0.1853` n `12`; crypto_alt avg `1.0791` n `232`; crypto_major avg `2.5978` n `8`; equity avg `0.4553` n `133`; fx avg `-0.0652` n `6`; index avg `0.1128` n `26`; metal avg `0.3777` n `20`; unknown avg `23.3486` n `790`
- 24h: commodity avg `0.3984` n `12`; crypto_alt avg `2.4724` n `232`; crypto_major avg `3.3307` n `8`; equity avg `0.689` n `133`; fx avg `-0.3117` n `6`; index avg `-0.0296` n `26`; metal avg `0.5287` n `20`; unknown avg `15.3423` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0396`, n `668`, weak_sample_signal
