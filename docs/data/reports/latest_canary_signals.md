# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T04:07:28.166139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.03` n `12`; crypto_alt avg `-0.0489` n `230`; crypto_major avg `0.0468` n `8`; equity avg `0.0255` n `108`; fx avg `0.0154` n `6`; index avg `0.0026` n `25`; metal avg `0.0351` n `20`; unknown avg `0.0757` n `782`
- 1h: commodity avg `-0.1124` n `12`; crypto_alt avg `0.0507` n `230`; crypto_major avg `0.0612` n `8`; equity avg `-0.1192` n `108`; fx avg `0.0155` n `6`; index avg `-0.0264` n `25`; metal avg `-0.082` n `20`; unknown avg `-0.0486` n `782`
- 4h: commodity avg `0.0105` n `12`; crypto_alt avg `-0.3662` n `230`; crypto_major avg `-0.6475` n `8`; equity avg `-0.2664` n `108`; fx avg `-0.0471` n `6`; index avg `-0.1618` n `25`; metal avg `-0.0166` n `20`; unknown avg `-0.2921` n `782`
- 24h: commodity avg `0.0322` n `12`; crypto_alt avg `-0.0294` n `230`; crypto_major avg `-0.0906` n `8`; equity avg `-1.9628` n `108`; fx avg `0.0341` n `6`; index avg `-0.3627` n `25`; metal avg `0.495` n `20`; unknown avg `0.8861` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
