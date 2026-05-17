# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T08:22:16.483168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.3889` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.1307` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.118` n `228`; crypto_major avg `-0.1079` n `8`; equity avg `-0.0158` n `65`; fx avg `0.0006` n `5`; index avg `0.0119` n `23`; metal avg `-0.0039` n `18`; unknown avg `-0.0395` n `383`
- 1h: commodity avg `-0.0821` n `12`; crypto_alt avg `-0.0505` n `228`; crypto_major avg `-0.0346` n `8`; equity avg `-0.0111` n `65`; fx avg `0.0023` n `5`; index avg `-0.0017` n `23`; metal avg `0.0117` n `18`; unknown avg `-0.01` n `383`
- 4h: commodity avg `1.7174` n `12`; crypto_alt avg `-8.9457` n `228`; crypto_major avg `-2.6715` n `8`; equity avg `-2.8893` n `65`; fx avg `-0.1717` n `5`; index avg `-1.7979` n `23`; metal avg `-5.8022` n `18`; unknown avg `550.1082` n `367`
- 24h: commodity avg `1.7174` n `12`; crypto_alt avg `-8.9457` n `228`; crypto_major avg `-2.6715` n `8`; equity avg `-2.8893` n `65`; fx avg `-0.1717` n `5`; index avg `-1.7979` n `23`; metal avg `-5.8022` n `18`; unknown avg `550.1082` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
