# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T22:44:22.677328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.297` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0283` n `12`; crypto_alt avg `-0.3069` n `228`; crypto_major avg `-0.2474` n `8`; equity avg `-0.0` n `66`; fx avg `-0.0093` n `6`; index avg `-0.0148` n `23`; metal avg `0.1452` n `18`; unknown avg `-0.245` n `383`
- 1h: commodity avg `0.0266` n `12`; crypto_alt avg `0.1231` n `228`; crypto_major avg `-0.0991` n `8`; equity avg `0.1696` n `66`; fx avg `0.0052` n `6`; index avg `0.049` n `23`; metal avg `0.3027` n `18`; unknown avg `-0.3255` n `383`
- 4h: commodity avg `-0.6287` n `12`; crypto_alt avg `2.0876` n `228`; crypto_major avg `1.6683` n `8`; equity avg `1.3023` n `66`; fx avg `0.0195` n `6`; index avg `0.6734` n `23`; metal avg `1.0109` n `18`; unknown avg `0.7605` n `383`
- 24h: commodity avg `0.82` n `12`; crypto_alt avg `-0.7287` n `228`; crypto_major avg `-1.2945` n `8`; equity avg `-0.9304` n `66`; fx avg `0.1713` n `6`; index avg `-0.2077` n `23`; metal avg `0.8152` n `18`; unknown avg `-0.0802` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
