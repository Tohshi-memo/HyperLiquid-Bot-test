# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T17:22:31.885891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.0325` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0286` n `12`; crypto_alt avg `0.2337` n `228`; crypto_major avg `0.4003` n `8`; equity avg `0.1475` n `88`; fx avg `0.0004` n `6`; index avg `0.0437` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.0077` n `763`
- 1h: commodity avg `-0.005` n `12`; crypto_alt avg `-0.1311` n `228`; crypto_major avg `-0.0083` n `8`; equity avg `-0.2094` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0424` n `25`; metal avg `-0.1287` n `20`; unknown avg `-0.0198` n `763`
- 4h: commodity avg `-0.2012` n `12`; crypto_alt avg `1.3001` n `228`; crypto_major avg `1.8313` n `8`; equity avg `0.7286` n `88`; fx avg `-0.0126` n `6`; index avg `-0.1286` n `25`; metal avg `0.4148` n `20`; unknown avg `1.17` n `763`
- 24h: commodity avg `-0.6246` n `12`; crypto_alt avg `2.049` n `228`; crypto_major avg `2.0646` n `8`; equity avg `-0.4397` n `88`; fx avg `-0.0059` n `6`; index avg `-0.4231` n `25`; metal avg `0.3442` n `20`; unknown avg `0.64` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
