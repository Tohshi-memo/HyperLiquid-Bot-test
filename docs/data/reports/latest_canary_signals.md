# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T20:22:26.369198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.0201` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.5989` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `-0.0561` n `228`; crypto_major avg `0.1867` n `8`; equity avg `0.6101` n `86`; fx avg `0.001` n `6`; index avg `0.1349` n `23`; metal avg `-0.0448` n `20`; unknown avg `-0.0607` n `764`
- 1h: commodity avg `-0.0519` n `12`; crypto_alt avg `1.9119` n `228`; crypto_major avg `1.9682` n `8`; equity avg `2.3175` n `86`; fx avg `-0.0075` n `6`; index avg `0.5454` n `23`; metal avg `0.3693` n `20`; unknown avg `3.5105` n `764`
- 4h: commodity avg `-0.1427` n `12`; crypto_alt avg `-0.4306` n `228`; crypto_major avg `0.1536` n `8`; equity avg `0.6205` n `86`; fx avg `0.0169` n `6`; index avg `0.2791` n `23`; metal avg `-0.2433` n `20`; unknown avg `-0.0623` n `764`
- 24h: commodity avg `-0.6274` n `12`; crypto_alt avg `-2.8163` n `228`; crypto_major avg `-2.3689` n `8`; equity avg `3.7019` n `86`; fx avg `0.0547` n `6`; index avg `0.4777` n `23`; metal avg `-1.6457` n `20`; unknown avg `-0.5685` n `724`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
