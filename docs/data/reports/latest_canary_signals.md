# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T17:37:32.916900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3517` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.1575` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9887` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0238` n `12`; crypto_alt avg `0.0508` n `234`; crypto_major avg `-0.0891` n `8`; equity avg `0.087` n `140`; fx avg `0.0003` n `6`; index avg `0.0063` n `26`; metal avg `0.0353` n `20`; unknown avg `13.1413` n `922`
- 1h: commodity avg `-0.0294` n `12`; crypto_alt avg `-0.1701` n `234`; crypto_major avg `-0.338` n `8`; equity avg `0.2511` n `140`; fx avg `-0.0022` n `6`; index avg `0.0406` n `26`; metal avg `0.0607` n `20`; unknown avg `11.7225` n `920`
- 4h: commodity avg `-0.1836` n `12`; crypto_alt avg `1.1112` n `234`; crypto_major avg `2.1681` n `8`; equity avg `0.0106` n `140`; fx avg `-0.0512` n `6`; index avg `-0.0693` n `26`; metal avg `0.1794` n `20`; unknown avg `11.557` n `884`
- 24h: commodity avg `-0.2131` n `12`; crypto_alt avg `5.673` n `234`; crypto_major avg `5.8668` n `8`; equity avg `0.7228` n `140`; fx avg `0.1804` n `6`; index avg `-0.1112` n `26`; metal avg `0.3259` n `20`; unknown avg `6.9034` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
