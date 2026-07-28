# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T11:22:28.588911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `12`; crypto_alt avg `0.2413` n `230`; crypto_major avg `0.1495` n `8`; equity avg `0.0802` n `102`; fx avg `0.0053` n `6`; index avg `0.0333` n `25`; metal avg `0.0263` n `20`; unknown avg `0.0327` n `774`
- 1h: commodity avg `-0.0487` n `12`; crypto_alt avg `-0.0655` n `230`; crypto_major avg `-0.1037` n `8`; equity avg `-0.4026` n `102`; fx avg `0.0048` n `6`; index avg `-0.0271` n `25`; metal avg `0.0432` n `20`; unknown avg `-0.0505` n `774`
- 4h: commodity avg `-0.0371` n `12`; crypto_alt avg `-0.264` n `230`; crypto_major avg `-0.4036` n `8`; equity avg `-0.682` n `102`; fx avg `-0.0345` n `6`; index avg `-0.1205` n `25`; metal avg `-0.2557` n `20`; unknown avg `-0.0984` n `774`
- 24h: commodity avg `-0.5837` n `12`; crypto_alt avg `-3.6184` n `230`; crypto_major avg `-3.8627` n `8`; equity avg `-4.5597` n `102`; fx avg `-0.1756` n `6`; index avg `-0.913` n `25`; metal avg `-0.654` n `20`; unknown avg `1225.2859` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
