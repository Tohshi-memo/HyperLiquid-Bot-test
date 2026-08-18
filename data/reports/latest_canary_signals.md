# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T06:22:53.428301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `0.429` n `230`; crypto_major avg `0.2987` n `8`; equity avg `0.2816` n `114`; fx avg `0.0117` n `6`; index avg `0.0805` n `25`; metal avg `0.1011` n `20`; unknown avg `0.1994` n `793`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `0.2531` n `230`; crypto_major avg `0.1287` n `8`; equity avg `-0.1008` n `114`; fx avg `0.0126` n `6`; index avg `-0.0467` n `25`; metal avg `0.0599` n `20`; unknown avg `0.0196` n `761`
- 4h: commodity avg `0.0831` n `12`; crypto_alt avg `-0.2129` n `230`; crypto_major avg `0.1554` n `8`; equity avg `-0.4397` n `114`; fx avg `-0.001` n `6`; index avg `-0.1704` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0236` n `761`
- 24h: commodity avg `0.7976` n `12`; crypto_alt avg `-1.0472` n `230`; crypto_major avg `0.1308` n `8`; equity avg `-1.5445` n `114`; fx avg `-0.0102` n `6`; index avg `-0.4137` n `25`; metal avg `-0.1544` n `20`; unknown avg `0.0243` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1858`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
