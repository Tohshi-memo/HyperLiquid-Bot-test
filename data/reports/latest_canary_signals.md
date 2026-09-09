# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T23:52:26.644138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.1494` n `233`; crypto_major avg `0.0981` n `8`; equity avg `0.0131` n `134`; fx avg `0.0151` n `6`; index avg `0.0146` n `26`; metal avg `-0.0203` n `20`; unknown avg `0.0575` n `797`
- 1h: commodity avg `0.0154` n `12`; crypto_alt avg `0.9391` n `233`; crypto_major avg `0.561` n `8`; equity avg `0.0359` n `134`; fx avg `0.0151` n `6`; index avg `-0.0032` n `26`; metal avg `-0.037` n `20`; unknown avg `1.9527` n `795`
- 4h: commodity avg `0.0942` n `12`; crypto_alt avg `-1.3476` n `233`; crypto_major avg `-0.7186` n `8`; equity avg `-0.243` n `134`; fx avg `0.0028` n `6`; index avg `0.0034` n `26`; metal avg `-0.0298` n `20`; unknown avg `20.436` n `691`
- 24h: commodity avg `0.0953` n `12`; crypto_alt avg `-2.7421` n `233`; crypto_major avg `-1.7935` n `8`; equity avg `-0.4441` n `134`; fx avg `0.0106` n `6`; index avg `-0.092` n `26`; metal avg `0.517` n `20`; unknown avg `1.2594` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
