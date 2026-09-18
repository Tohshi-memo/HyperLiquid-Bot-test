# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T17:22:30.026534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7272` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5063` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.482` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0386` n `12`; crypto_alt avg `0.1798` n `234`; crypto_major avg `0.1659` n `8`; equity avg `0.0196` n `140`; fx avg `0.0072` n `6`; index avg `0.0031` n `26`; metal avg `-0.0048` n `20`; unknown avg `2.2108` n `928`
- 1h: commodity avg `-0.1697` n `12`; crypto_alt avg `-0.1103` n `234`; crypto_major avg `-0.0959` n `8`; equity avg `0.1188` n `140`; fx avg `-0.0125` n `6`; index avg `0.0292` n `26`; metal avg `0.0711` n `20`; unknown avg `2.194` n `920`
- 4h: commodity avg `-0.1711` n `12`; crypto_alt avg `1.2976` n `234`; crypto_major avg `2.5561` n `8`; equity avg `0.0741` n `140`; fx avg `-0.0467` n `6`; index avg `-0.076` n `26`; metal avg `0.0498` n `20`; unknown avg `0.714` n `884`
- 24h: commodity avg `-0.2386` n `12`; crypto_alt avg `5.5594` n `234`; crypto_major avg `5.9467` n `8`; equity avg `0.538` n `140`; fx avg `0.1794` n `6`; index avg `-0.1256` n `26`; metal avg `0.2739` n `20`; unknown avg `1.4135` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
