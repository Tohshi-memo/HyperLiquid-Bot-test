# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T15:22:49.288891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0629` n `12`; crypto_alt avg `-0.1608` n `232`; crypto_major avg `0.0071` n `8`; equity avg `-0.0164` n `134`; fx avg `-0.0123` n `6`; index avg `-0.0074` n `26`; metal avg `0.0012` n `20`; unknown avg `0.2428` n `796`
- 1h: commodity avg `0.0214` n `12`; crypto_alt avg `-0.3984` n `232`; crypto_major avg `-0.2891` n `8`; equity avg `-0.007` n `134`; fx avg `-0.0105` n `6`; index avg `-0.0122` n `26`; metal avg `0.0487` n `20`; unknown avg `0.0082` n `794`
- 4h: commodity avg `0.0106` n `12`; crypto_alt avg `0.0179` n `232`; crypto_major avg `-0.4461` n `8`; equity avg `-0.0012` n `134`; fx avg `-0.0409` n `6`; index avg `0.0169` n `26`; metal avg `0.1762` n `20`; unknown avg `6684.185` n `748`
- 24h: commodity avg `0.2079` n `12`; crypto_alt avg `1.0414` n `232`; crypto_major avg `-0.6575` n `8`; equity avg `0.4923` n `134`; fx avg `-0.1201` n `6`; index avg `0.0392` n `26`; metal avg `0.004` n `20`; unknown avg `218.1424` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
