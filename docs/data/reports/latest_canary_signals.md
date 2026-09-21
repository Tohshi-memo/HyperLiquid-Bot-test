# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T10:07:39.466662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5455` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4089` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5438` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `-0.0139` n `234`; crypto_major avg `-0.0401` n `8`; equity avg `-0.0114` n `140`; fx avg `0.008` n `6`; index avg `0.0012` n `26`; metal avg `0.0273` n `20`; unknown avg `-0.0223` n `940`
- 1h: commodity avg `-0.0717` n `12`; crypto_alt avg `0.0877` n `234`; crypto_major avg `0.1603` n `8`; equity avg `0.0085` n `140`; fx avg `0.0143` n `6`; index avg `0.0039` n `26`; metal avg `-0.0343` n `20`; unknown avg `1.2453` n `940`
- 4h: commodity avg `-0.107` n `12`; crypto_alt avg `1.8334` n `234`; crypto_major avg `2.4385` n `8`; equity avg `0.8947` n `140`; fx avg `-0.0725` n `6`; index avg `0.1201` n `26`; metal avg `0.0296` n `20`; unknown avg `1.6676` n `912`
- 24h: commodity avg `-0.6328` n `12`; crypto_alt avg `6.467` n `234`; crypto_major avg `5.4743` n `8`; equity avg `2.0581` n `140`; fx avg `-0.0875` n `6`; index avg `0.3572` n `26`; metal avg `0.0028` n `20`; unknown avg `7.9553` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
