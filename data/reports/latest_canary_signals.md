# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T21:52:27.989111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1393` n `12`; crypto_alt avg `0.518` n `228`; crypto_major avg `0.4492` n `8`; equity avg `0.0752` n `74`; fx avg `-0.0712` n `6`; index avg `-0.0108` n `23`; metal avg `-0.0123` n `18`; unknown avg `1.0566` n `644`
- 1h: commodity avg `0.0224` n `12`; crypto_alt avg `0.5781` n `228`; crypto_major avg `0.6783` n `8`; equity avg `0.1048` n `74`; fx avg `-0.0676` n `6`; index avg `0.111` n `23`; metal avg `0.7505` n `18`; unknown avg `4.82` n `644`
- 4h: commodity avg `0.1074` n `12`; crypto_alt avg `0.2821` n `228`; crypto_major avg `0.8593` n `8`; equity avg `0.3691` n `74`; fx avg `-0.0414` n `6`; index avg `0.2878` n `23`; metal avg `0.7373` n `18`; unknown avg `1.1134` n `644`
- 24h: commodity avg `-0.6175` n `12`; crypto_alt avg `2.6956` n `228`; crypto_major avg `1.4351` n `8`; equity avg `0.528` n `74`; fx avg `0.0079` n `6`; index avg `0.6734` n `23`; metal avg `1.0748` n `18`; unknown avg `-0.2432` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
