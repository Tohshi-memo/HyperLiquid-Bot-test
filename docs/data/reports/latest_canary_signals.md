# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T09:52:34.586750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `13`; crypto_alt avg `-0.0695` n `237`; crypto_major avg `-0.0683` n `8`; equity avg `-0.0455` n `151`; fx avg `0.0029` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0437` n `20`; unknown avg `-0.1645` n `1198`
- 1h: commodity avg `0.0551` n `13`; crypto_alt avg `-0.1625` n `237`; crypto_major avg `-0.0975` n `8`; equity avg `-0.3318` n `151`; fx avg `-0.0038` n `6`; index avg `-0.0513` n `26`; metal avg `-0.0949` n `20`; unknown avg `-0.3339` n `1196`
- 4h: commodity avg `0.2513` n `13`; crypto_alt avg `-0.8178` n `237`; crypto_major avg `-0.6243` n `8`; equity avg `-0.409` n `151`; fx avg `0.0019` n `6`; index avg `-0.0656` n `26`; metal avg `-0.0537` n `20`; unknown avg `2.3574` n `1160`
- 24h: commodity avg `0.2817` n `13`; crypto_alt avg `-0.7544` n `237`; crypto_major avg `-1.4477` n `8`; equity avg `-1.9163` n `151`; fx avg `0.011` n `6`; index avg `-0.2877` n `26`; metal avg `-0.3149` n `20`; unknown avg `0.4269` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
