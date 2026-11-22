# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T11:37:38.217187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1829` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1134` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.1312` n `239`; crypto_major avg `-0.0569` n `8`; equity avg `0.006` n `166`; fx avg `-0.006` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0141` n `20`; unknown avg `189.887` n `1263`
- 1h: commodity avg `-0.0092` n `13`; crypto_alt avg `0.105` n `239`; crypto_major avg `0.1706` n `8`; equity avg `0.1448` n `166`; fx avg `-0.0107` n `6`; index avg `-0.0066` n `27`; metal avg `0.0085` n `20`; unknown avg `158.8072` n `1259`
- 4h: commodity avg `0.0638` n `13`; crypto_alt avg `1.9667` n `239`; crypto_major avg `2.2467` n `8`; equity avg `1.2077` n `166`; fx avg `-0.032` n `6`; index avg `0.1015` n `27`; metal avg `0.1333` n `20`; unknown avg `273.2145` n `1141`
- 24h: commodity avg `0.0506` n `13`; crypto_alt avg `2.9057` n `239`; crypto_major avg `3.4729` n `8`; equity avg `1.7157` n `166`; fx avg `-0.0239` n `6`; index avg `0.1973` n `27`; metal avg `0.1508` n `20`; unknown avg `0.2276` n `1078`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
