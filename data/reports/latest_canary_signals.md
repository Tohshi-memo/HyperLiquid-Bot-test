# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T16:52:43.781330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.304` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.2287` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.8154` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0448` n `12`; crypto_alt avg `0.5124` n `230`; crypto_major avg `0.5687` n `8`; equity avg `0.1331` n `121`; fx avg `-0.0146` n `6`; index avg `0.0234` n `25`; metal avg `0.0294` n `20`; unknown avg `0.3685` n `792`
- 1h: commodity avg `-0.1112` n `12`; crypto_alt avg `0.5266` n `230`; crypto_major avg `1.0842` n `8`; equity avg `0.0167` n `121`; fx avg `0.0086` n `6`; index avg `0.0469` n `25`; metal avg `-0.0146` n `20`; unknown avg `0.3917` n `792`
- 4h: commodity avg `-0.157` n `12`; crypto_alt avg `1.77` n `230`; crypto_major avg `3.147` n `8`; equity avg `-0.0817` n `121`; fx avg `0.0065` n `6`; index avg `0.0857` n `25`; metal avg `0.3316` n `20`; unknown avg `0.6909` n `792`
- 24h: commodity avg `-0.154` n `12`; crypto_alt avg `6.3531` n `230`; crypto_major avg `10.5721` n `8`; equity avg `-0.6997` n `121`; fx avg `0.1888` n `6`; index avg `-0.0022` n `25`; metal avg `0.2586` n `20`; unknown avg `2.8874` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.21`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
