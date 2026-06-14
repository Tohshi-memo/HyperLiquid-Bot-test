# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T03:52:32.706594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `0.0475` n `228`; crypto_major avg `0.0182` n `8`; equity avg `0.0075` n `74`; fx avg `0.0031` n `6`; index avg `0.0328` n `23`; metal avg `-0.0056` n `18`; unknown avg `3.5746` n `645`
- 1h: commodity avg `-0.0293` n `12`; crypto_alt avg `0.166` n `228`; crypto_major avg `-0.0024` n `8`; equity avg `0.0124` n `74`; fx avg `0.0157` n `6`; index avg `0.0109` n `23`; metal avg `-0.015` n `18`; unknown avg `-1.3716` n `645`
- 4h: commodity avg `0.0313` n `12`; crypto_alt avg `0.124` n `228`; crypto_major avg `0.0934` n `8`; equity avg `0.1229` n `74`; fx avg `0.0091` n `6`; index avg `-0.0233` n `23`; metal avg `0.0103` n `18`; unknown avg `-1.5122` n `629`
- 24h: commodity avg `-0.6609` n `12`; crypto_alt avg `1.6124` n `228`; crypto_major avg `1.7351` n `8`; equity avg `0.6311` n `74`; fx avg `0.0232` n `6`; index avg `0.2156` n `23`; metal avg `0.3042` n `18`; unknown avg `-1.6607` n `595`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
