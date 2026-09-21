# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T01:22:27.866299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9182` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0328` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0655` n `12`; crypto_alt avg `0.4419` n `234`; crypto_major avg `0.3534` n `8`; equity avg `-0.0202` n `140`; fx avg `-0.0404` n `6`; index avg `-0.0064` n `26`; metal avg `-0.06` n `20`; unknown avg `-0.3206` n `944`
- 1h: commodity avg `-0.3202` n `12`; crypto_alt avg `0.2073` n `234`; crypto_major avg `0.3566` n `8`; equity avg `0.342` n `140`; fx avg `-0.042` n `6`; index avg `0.0362` n `26`; metal avg `0.1397` n `20`; unknown avg `0.6153` n `941`
- 4h: commodity avg `-0.7366` n `12`; crypto_alt avg `1.7362` n `234`; crypto_major avg `2.1816` n `8`; equity avg `0.9886` n `140`; fx avg `0.0124` n `6`; index avg `0.1441` n `26`; metal avg `0.1488` n `20`; unknown avg `3.7626` n `907`
- 24h: commodity avg `-0.5529` n `12`; crypto_alt avg `2.1172` n `234`; crypto_major avg `2.0666` n `8`; equity avg `0.8523` n `140`; fx avg `-0.0249` n `6`; index avg `0.1189` n `26`; metal avg `0.0758` n `20`; unknown avg `4.197` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
