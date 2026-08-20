# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T17:22:38.044430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.2425` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.0783` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6402` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `0.0267` n `230`; crypto_major avg `-0.1342` n `8`; equity avg `-0.0771` n `121`; fx avg `0.0082` n `6`; index avg `-0.0214` n `25`; metal avg `-0.0285` n `20`; unknown avg `0.0773` n `792`
- 1h: commodity avg `-0.0866` n `12`; crypto_alt avg `0.8397` n `230`; crypto_major avg `1.2967` n `8`; equity avg `-0.0018` n `121`; fx avg `-0.0114` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0064` n `20`; unknown avg `1.1657` n `792`
- 4h: commodity avg `-0.1454` n `12`; crypto_alt avg `1.7877` n `230`; crypto_major avg `2.9329` n `8`; equity avg `-0.3096` n `121`; fx avg `0.0399` n `6`; index avg `0.0381` n `25`; metal avg `0.2927` n `20`; unknown avg `1.2704` n `792`
- 24h: commodity avg `-0.1075` n `12`; crypto_alt avg `6.9228` n `230`; crypto_major avg `11.6053` n `8`; equity avg `-0.3706` n `121`; fx avg `0.1977` n `6`; index avg `0.0026` n `25`; metal avg `0.3018` n `20`; unknown avg `3.8138` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
