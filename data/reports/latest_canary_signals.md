# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T17:07:39.966477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7724` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6364` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.5077` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.0102` n `234`; crypto_major avg `-0.0339` n `8`; equity avg `0.0169` n `140`; fx avg `-0.0107` n `6`; index avg `0.0116` n `26`; metal avg `0.032` n `20`; unknown avg `10.1307` n `924`
- 1h: commodity avg `-0.1354` n `12`; crypto_alt avg `-0.2659` n `234`; crypto_major avg `-0.2127` n `8`; equity avg `0.0349` n `140`; fx avg `-0.0004` n `6`; index avg `0.0234` n `26`; metal avg `0.1473` n `20`; unknown avg `0.8531` n `920`
- 4h: commodity avg `-0.0872` n `12`; crypto_alt avg `1.322` n `234`; crypto_major avg `2.6852` n `8`; equity avg `0.1775` n `140`; fx avg `-0.0482` n `6`; index avg `-0.0694` n `26`; metal avg `0.0488` n `20`; unknown avg `1.1115` n `884`
- 24h: commodity avg `-0.2055` n `12`; crypto_alt avg `5.2777` n `234`; crypto_major avg `5.7184` n `8`; equity avg `0.4133` n `140`; fx avg `0.1759` n `6`; index avg `-0.1456` n `26`; metal avg `0.2118` n `20`; unknown avg `1.7111` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
