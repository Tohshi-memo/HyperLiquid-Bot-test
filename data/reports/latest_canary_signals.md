# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T16:22:31.627361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.965` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.8895` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.8377` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `0.0234` n `234`; crypto_major avg `0.0485` n `8`; equity avg `-0.0642` n `140`; fx avg `0.0193` n `6`; index avg `-0.0026` n `26`; metal avg `0.0712` n `20`; unknown avg `12.8189` n `928`
- 1h: commodity avg `-0.0689` n `12`; crypto_alt avg `0.3703` n `234`; crypto_major avg `0.1527` n `8`; equity avg `0.0629` n `140`; fx avg `-0.0076` n `6`; index avg `-0.0203` n `26`; metal avg `0.0773` n `20`; unknown avg `12.229` n `914`
- 4h: commodity avg `0.1162` n `12`; crypto_alt avg `1.7694` n `234`; crypto_major avg `2.9539` n `8`; equity avg `0.0644` n `140`; fx avg `-0.0423` n `6`; index avg `-0.0932` n `26`; metal avg `-0.0111` n `20`; unknown avg `12.1331` n `884`
- 24h: commodity avg `0.0977` n `12`; crypto_alt avg `6.1155` n `234`; crypto_major avg `6.2502` n `8`; equity avg `0.4672` n `140`; fx avg `0.2176` n `6`; index avg `-0.1469` n `26`; metal avg `0.1602` n `20`; unknown avg `6.893` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
