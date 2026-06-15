# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T12:52:38.230645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.29` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.4781` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0913` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7834` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0956` n `12`; crypto_alt avg `0.2141` n `228`; crypto_major avg `0.2686` n `8`; equity avg `0.0635` n `74`; fx avg `0.0111` n `6`; index avg `0.0311` n `23`; metal avg `0.0996` n `18`; unknown avg `-0.2347` n `689`
- 1h: commodity avg `-0.0003` n `12`; crypto_alt avg `0.2368` n `228`; crypto_major avg `0.2833` n `8`; equity avg `-0.1649` n `74`; fx avg `-0.0136` n `6`; index avg `-0.0337` n `23`; metal avg `0.1678` n `18`; unknown avg `0.0035` n `689`
- 4h: commodity avg `0.1029` n `12`; crypto_alt avg `1.5238` n `228`; crypto_major avg `2.1942` n `8`; equity avg `-0.2839` n `74`; fx avg `0.0156` n `6`; index avg `0.0294` n `23`; metal avg `0.4108` n `18`; unknown avg `0.1664` n `689`
- 24h: commodity avg `-1.2022` n `12`; crypto_alt avg `5.1884` n `228`; crypto_major avg `5.5774` n `8`; equity avg `1.6198` n `74`; fx avg `0.0219` n `6`; index avg `0.9122` n `23`; metal avg `2.7925` n `18`; unknown avg `1.3659` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
