# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T07:37:15.545152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-4.2878` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-4.2878` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.2914` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `3.2914` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0251` n `12`; crypto_alt avg `0.0854` n `228`; crypto_major avg `0.1319` n `8`; equity avg `0.0157` n `65`; fx avg `0.0074` n `5`; index avg `-0.0074` n `23`; metal avg `0.0119` n `18`; unknown avg `0.0307` n `383`
- 1h: commodity avg `1.7775` n `12`; crypto_alt avg `-8.8263` n `228`; crypto_major avg `-2.5103` n `8`; equity avg `-2.8654` n `65`; fx avg `-0.1666` n `5`; index avg `-1.8035` n `23`; metal avg `-5.8017` n `18`; unknown avg `550.0669` n `367`
- 4h: commodity avg `1.7775` n `12`; crypto_alt avg `-8.8263` n `228`; crypto_major avg `-2.5103` n `8`; equity avg `-2.8654` n `65`; fx avg `-0.1666` n `5`; index avg `-1.8035` n `23`; metal avg `-5.8017` n `18`; unknown avg `550.0669` n `367`
- 24h: commodity avg `1.7775` n `12`; crypto_alt avg `-8.8263` n `228`; crypto_major avg `-2.5103` n `8`; equity avg `-2.8654` n `65`; fx avg `-0.1666` n `5`; index avg `-1.8035` n `23`; metal avg `-5.8017` n `18`; unknown avg `550.0669` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1399`, n `670`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1187`, n `670`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.095`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `670`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `670`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0741`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `670`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0698`, n `670`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0622`, n `670`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0618`, n `670`, weak_sample_signal
