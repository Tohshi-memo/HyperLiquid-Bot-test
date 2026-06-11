# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T05:22:29.488498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0695` n `12`; crypto_alt avg `0.12` n `228`; crypto_major avg `0.1773` n `8`; equity avg `0.0832` n `74`; fx avg `0.0124` n `6`; index avg `0.0017` n `23`; metal avg `0.031` n `18`; unknown avg `-0.1183` n `550`
- 1h: commodity avg `-0.3463` n `12`; crypto_alt avg `0.3938` n `228`; crypto_major avg `0.0984` n `8`; equity avg `0.1805` n `74`; fx avg `0.002` n `6`; index avg `0.0117` n `23`; metal avg `0.0242` n `18`; unknown avg `-0.0316` n `550`
- 4h: commodity avg `-0.3767` n `12`; crypto_alt avg `1.5539` n `228`; crypto_major avg `0.9273` n `8`; equity avg `0.0748` n `74`; fx avg `-0.011` n `6`; index avg `0.1154` n `23`; metal avg `-0.2793` n `18`; unknown avg `3.5376` n `550`
- 24h: commodity avg `1.5095` n `12`; crypto_alt avg `1.9588` n `228`; crypto_major avg `1.2388` n `8`; equity avg `0.1834` n `74`; fx avg `0.0214` n `6`; index avg `-0.295` n `23`; metal avg `-0.2857` n `18`; unknown avg `2.7862` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
