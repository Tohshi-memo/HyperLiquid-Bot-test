# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T17:07:27.844061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2119` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.7408` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1514` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0971` n `12`; crypto_alt avg `-0.0989` n `232`; crypto_major avg `-0.1602` n `8`; equity avg `-0.0164` n `133`; fx avg `0.0097` n `6`; index avg `-0.0027` n `26`; metal avg `0.0273` n `20`; unknown avg `2.5284` n `790`
- 1h: commodity avg `0.1926` n `12`; crypto_alt avg `0.1669` n `232`; crypto_major avg `0.1107` n `8`; equity avg `0.1568` n `133`; fx avg `0.0294` n `6`; index avg `0.0161` n `26`; metal avg `0.0096` n `20`; unknown avg `24.4056` n `790`
- 4h: commodity avg `-0.1742` n `12`; crypto_alt avg `2.0791` n `232`; crypto_major avg `3.0377` n `8`; equity avg `0.8863` n `133`; fx avg `0.0453` n `6`; index avg `0.182` n `26`; metal avg `0.2969` n `20`; unknown avg `9.9519` n `790`
- 24h: commodity avg `0.0472` n `12`; crypto_alt avg `4.4665` n `232`; crypto_major avg `5.5689` n `8`; equity avg `1.9748` n `133`; fx avg `-0.2598` n `6`; index avg `0.196` n `26`; metal avg `0.9562` n `20`; unknown avg `24.9768` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
