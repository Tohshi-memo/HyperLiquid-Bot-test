# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T15:37:29.087472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2424` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1348` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6163` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0474` n `13`; crypto_alt avg `-0.2027` n `239`; crypto_major avg `-0.216` n `8`; equity avg `-0.053` n `166`; fx avg `-0.0023` n `6`; index avg `-0.0046` n `27`; metal avg `-0.0212` n `20`; unknown avg `5.367` n `1258`
- 1h: commodity avg `-0.0467` n `13`; crypto_alt avg `-0.0451` n `239`; crypto_major avg `-0.1898` n `8`; equity avg `0.0083` n `166`; fx avg `0.0066` n `6`; index avg `-0.0206` n `27`; metal avg `-0.0101` n `20`; unknown avg `204.5523` n `1254`
- 4h: commodity avg `0.0091` n `13`; crypto_alt avg `2.1843` n `239`; crypto_major avg `2.2515` n `8`; equity avg `0.6352` n `166`; fx avg `0.0095` n `6`; index avg `0.0665` n `27`; metal avg `0.1167` n `20`; unknown avg `203.3661` n `1240`
- 24h: commodity avg `0.7297` n `13`; crypto_alt avg `0.9203` n `239`; crypto_major avg `0.6139` n `8`; equity avg `-1.2726` n `166`; fx avg `-0.0881` n `6`; index avg `-0.2346` n `27`; metal avg `-0.1076` n `20`; unknown avg `0.2661` n `1139`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
