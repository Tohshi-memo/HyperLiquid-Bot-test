# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T21:52:31.020431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `13`; crypto_alt avg `0.0104` n `237`; crypto_major avg `-0.0183` n `8`; equity avg `-0.0176` n `151`; fx avg `0.0029` n `6`; index avg `0.0127` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.0469` n `1196`
- 1h: commodity avg `-0.0472` n `13`; crypto_alt avg `0.2785` n `237`; crypto_major avg `0.2587` n `8`; equity avg `0.0856` n `151`; fx avg `0.0023` n `6`; index avg `0.0186` n `26`; metal avg `0.0127` n `20`; unknown avg `1.4495` n `1182`
- 4h: commodity avg `-0.3652` n `13`; crypto_alt avg `0.4077` n `237`; crypto_major avg `0.4185` n `8`; equity avg `0.1753` n `151`; fx avg `-0.0062` n `6`; index avg `0.038` n `26`; metal avg `-0.0376` n `20`; unknown avg `1.5445` n `1122`
- 24h: commodity avg `-0.3069` n `13`; crypto_alt avg `2.3837` n `237`; crypto_major avg `1.7761` n `8`; equity avg `2.4894` n `151`; fx avg `0.0221` n `6`; index avg `0.5278` n `26`; metal avg `0.0906` n `20`; unknown avg `4.1123` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
