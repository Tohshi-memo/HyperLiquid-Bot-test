# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T09:22:24.958643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.1962` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.8751` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.5488` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0328` n `12`; crypto_alt avg `0.0719` n `230`; crypto_major avg `0.1935` n `8`; equity avg `0.0671` n `121`; fx avg `-0.0133` n `6`; index avg `0.0103` n `25`; metal avg `0.0216` n `20`; unknown avg `-0.0527` n `792`
- 1h: commodity avg `0.1483` n `12`; crypto_alt avg `0.5929` n `230`; crypto_major avg `1.3057` n `8`; equity avg `0.0422` n `121`; fx avg `0.0206` n `6`; index avg `-0.021` n `25`; metal avg `-0.0483` n `20`; unknown avg `0.007` n `792`
- 4h: commodity avg `0.313` n `12`; crypto_alt avg `1.9546` n `230`; crypto_major avg `2.8618` n `8`; equity avg `-0.3344` n `121`; fx avg `0.0542` n `6`; index avg `-0.0761` n `25`; metal avg `-0.0133` n `20`; unknown avg `0.476` n `776`
- 24h: commodity avg `0.163` n `12`; crypto_alt avg `7.4867` n `230`; crypto_major avg `12.8443` n `8`; equity avg `0.1965` n `120`; fx avg `0.148` n `6`; index avg `0.0547` n `25`; metal avg `0.9746` n `20`; unknown avg `2.2339` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
