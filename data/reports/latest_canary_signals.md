# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T05:22:32.691834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.042` n `228`; crypto_major avg `-0.175` n `8`; equity avg `0.0667` n `86`; fx avg `-0.0155` n `6`; index avg `0.0122` n `23`; metal avg `-0.0489` n `20`; unknown avg `21.836` n `765`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `1.1901` n `228`; crypto_major avg `1.2017` n `8`; equity avg `0.3785` n `86`; fx avg `-0.0321` n `6`; index avg `0.0482` n `23`; metal avg `-0.0012` n `20`; unknown avg `3.6764` n `765`
- 4h: commodity avg `-0.0629` n `12`; crypto_alt avg `1.1389` n `228`; crypto_major avg `0.9637` n `8`; equity avg `0.4032` n `86`; fx avg `-0.0226` n `6`; index avg `0.1466` n `23`; metal avg `-0.0181` n `20`; unknown avg `1.0822` n `748`
- 24h: commodity avg `-0.492` n `12`; crypto_alt avg `-1.0266` n `228`; crypto_major avg `-1.0096` n `8`; equity avg `-0.0248` n `86`; fx avg `0.021` n `6`; index avg `0.5189` n `23`; metal avg `-1.4849` n `20`; unknown avg `-0.4003` n `708`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
