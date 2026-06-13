# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T12:52:31.709886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0835` n `12`; crypto_alt avg `0.1515` n `228`; crypto_major avg `0.1514` n `8`; equity avg `0.0877` n `74`; fx avg `-0.0248` n `6`; index avg `0.0363` n `23`; metal avg `0.1466` n `18`; unknown avg `0.2701` n `644`
- 1h: commodity avg `-0.2041` n `12`; crypto_alt avg `0.2777` n `228`; crypto_major avg `0.4492` n `8`; equity avg `0.1607` n `74`; fx avg `0.0012` n `6`; index avg `0.1021` n `23`; metal avg `0.1327` n `18`; unknown avg `0.3656` n `644`
- 4h: commodity avg `-0.4101` n `12`; crypto_alt avg `0.7239` n `228`; crypto_major avg `0.6417` n `8`; equity avg `0.0832` n `74`; fx avg `0.0571` n `6`; index avg `0.1921` n `23`; metal avg `0.2231` n `18`; unknown avg `0.7273` n `635`
- 24h: commodity avg `-0.8588` n `12`; crypto_alt avg `1.1391` n `228`; crypto_major avg `0.5035` n `8`; equity avg `-0.0848` n `74`; fx avg `0.0357` n `6`; index avg `0.9469` n `23`; metal avg `1.0574` n `18`; unknown avg `28.1014` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
