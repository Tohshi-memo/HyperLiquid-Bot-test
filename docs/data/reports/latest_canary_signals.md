# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T14:22:26.888855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.4432` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.8506` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `0.3372` n `228`; crypto_major avg `0.5061` n `8`; equity avg `0.3057` n `86`; fx avg `-0.0109` n `6`; index avg `0.0563` n `23`; metal avg `0.1385` n `20`; unknown avg `-0.0174` n `765`
- 1h: commodity avg `-0.1448` n `12`; crypto_alt avg `1.8217` n `228`; crypto_major avg `2.2984` n `8`; equity avg `1.9745` n `86`; fx avg `-0.0225` n `6`; index avg `0.2792` n `23`; metal avg `0.4478` n `20`; unknown avg `0.4496` n `765`
- 4h: commodity avg `-0.0427` n `12`; crypto_alt avg `0.8341` n `228`; crypto_major avg `1.2155` n `8`; equity avg `1.4203` n `86`; fx avg `-0.0066` n `6`; index avg `0.1966` n `23`; metal avg `0.5598` n `20`; unknown avg `0.0682` n `765`
- 24h: commodity avg `-0.2965` n `12`; crypto_alt avg `1.5688` n `228`; crypto_major avg `2.3943` n `8`; equity avg `-0.491` n `86`; fx avg `0.0282` n `6`; index avg `-0.1933` n `23`; metal avg `0.8688` n `20`; unknown avg `0.8217` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3522`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
