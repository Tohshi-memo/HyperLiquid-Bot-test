# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T20:22:26.975956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `-0.0355` n `230`; crypto_major avg `0.0209` n `8`; equity avg `-0.0321` n `120`; fx avg `0.0042` n `6`; index avg `-0.0053` n `25`; metal avg `-0.0115` n `20`; unknown avg `-0.02` n `789`
- 1h: commodity avg `0.0509` n `12`; crypto_alt avg `-0.2051` n `230`; crypto_major avg `-0.0585` n `8`; equity avg `-0.054` n `120`; fx avg `-0.0029` n `6`; index avg `-0.0373` n `25`; metal avg `-0.1077` n `20`; unknown avg `-0.0518` n `789`
- 4h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.3454` n `230`; crypto_major avg `0.1533` n `8`; equity avg `-0.4276` n `120`; fx avg `0.0019` n `6`; index avg `-0.0464` n `25`; metal avg `-0.1584` n `20`; unknown avg `0.1586` n `789`
- 24h: commodity avg `0.2929` n `12`; crypto_alt avg `-0.5485` n `230`; crypto_major avg `0.3879` n `8`; equity avg `-4.3007` n `120`; fx avg `-0.0461` n `6`; index avg `-0.6992` n `25`; metal avg `-0.7765` n `20`; unknown avg `-0.2539` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
