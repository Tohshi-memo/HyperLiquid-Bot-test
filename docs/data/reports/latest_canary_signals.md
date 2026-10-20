# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T00:52:28.022707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `13`; crypto_alt avg `0.0277` n `237`; crypto_major avg `0.0016` n `8`; equity avg `-0.3496` n `151`; fx avg `-0.0245` n `6`; index avg `-0.0774` n `26`; metal avg `-0.0428` n `20`; unknown avg `-0.2575` n `1198`
- 1h: commodity avg `0.0032` n `13`; crypto_alt avg `-0.2989` n `237`; crypto_major avg `-0.3103` n `8`; equity avg `-0.7856` n `151`; fx avg `-0.0445` n `6`; index avg `-0.166` n `26`; metal avg `-0.0464` n `20`; unknown avg `-0.0819` n `1190`
- 4h: commodity avg `-0.0181` n `13`; crypto_alt avg `0.5412` n `237`; crypto_major avg `0.1812` n `8`; equity avg `-0.8466` n `151`; fx avg `-0.0603` n `6`; index avg `-0.1666` n `26`; metal avg `-0.0963` n `20`; unknown avg `3.5645` n `1168`
- 24h: commodity avg `0.1544` n `13`; crypto_alt avg `-0.0126` n `237`; crypto_major avg `-0.3287` n `8`; equity avg `-0.3955` n `151`; fx avg `-0.0889` n `6`; index avg `-0.0235` n `26`; metal avg `-0.2529` n `20`; unknown avg `5.0125` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
