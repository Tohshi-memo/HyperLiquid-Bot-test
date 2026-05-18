# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T16:00:08.439447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0096` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0973` n `12`; crypto_alt avg `0.038` n `228`; crypto_major avg `0.0596` n `8`; equity avg `0.0053` n `66`; fx avg `-0.0051` n `5`; index avg `0.0069` n `23`; metal avg `0.1057` n `18`; unknown avg `-0.0413` n `384`
- 1h: commodity avg `0.0709` n `12`; crypto_alt avg `0.4071` n `228`; crypto_major avg `0.3148` n `8`; equity avg `-0.1949` n `66`; fx avg `-0.0056` n `5`; index avg `-0.1109` n `23`; metal avg `0.3121` n `18`; unknown avg `-0.4002` n `384`
- 4h: commodity avg `0.6973` n `12`; crypto_alt avg `-0.9126` n `228`; crypto_major avg `-1.3123` n `8`; equity avg `-1.6786` n `66`; fx avg `-0.0155` n `5`; index avg `-0.4907` n `23`; metal avg `0.013` n `18`; unknown avg `0.364` n `383`
- 24h: commodity avg `0.9518` n `12`; crypto_alt avg `-2.8353` n `228`; crypto_major avg `-2.1965` n `8`; equity avg `-0.8595` n `66`; fx avg `0.05` n `5`; index avg `-0.4341` n `23`; metal avg `0.4505` n `18`; unknown avg `-0.3597` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
