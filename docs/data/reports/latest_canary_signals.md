# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T17:52:27.791134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `13`; crypto_alt avg `0.0122` n `237`; crypto_major avg `0.0411` n `8`; equity avg `0.0283` n `152`; fx avg `-0.0005` n `6`; index avg `0.0016` n `26`; metal avg `0.0052` n `20`; unknown avg `0.5817` n `1240`
- 1h: commodity avg `0.0306` n `13`; crypto_alt avg `0.4361` n `237`; crypto_major avg `0.2512` n `8`; equity avg `0.0995` n `152`; fx avg `0.0042` n `6`; index avg `0.0111` n `26`; metal avg `0.0254` n `20`; unknown avg `3.6986` n `1200`
- 4h: commodity avg `0.0151` n `13`; crypto_alt avg `1.0631` n `237`; crypto_major avg `0.6521` n `8`; equity avg `0.3709` n `152`; fx avg `-0.0145` n `6`; index avg `0.0403` n `26`; metal avg `0.0735` n `20`; unknown avg `1.212` n `1185`
- 24h: commodity avg `-0.1772` n `13`; crypto_alt avg `1.1127` n `237`; crypto_major avg `1.3943` n `8`; equity avg `0.8883` n `152`; fx avg `0.0245` n `6`; index avg `0.1522` n `26`; metal avg `0.1762` n `20`; unknown avg `10.745` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2261`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
