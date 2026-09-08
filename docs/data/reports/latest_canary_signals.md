# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T11:52:33.466412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.304` n `232`; crypto_major avg `-0.1689` n `8`; equity avg `-0.1249` n `134`; fx avg `0.0114` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0793` n `20`; unknown avg `0.5158` n `797`
- 1h: commodity avg `0.1102` n `12`; crypto_alt avg `-0.6568` n `232`; crypto_major avg `-0.5465` n `8`; equity avg `-0.0124` n `134`; fx avg `0.0313` n `6`; index avg `-0.0172` n `26`; metal avg `-0.0197` n `20`; unknown avg `1.1278` n `795`
- 4h: commodity avg `0.0342` n `11`; crypto_alt avg `0.008` n `232`; crypto_major avg `-0.0454` n `8`; equity avg `0.196` n `123`; fx avg `0.0473` n `5`; index avg `0.0595` n `20`; metal avg `0.0425` n `18`; unknown avg `0.4541` n `785`
- 24h: commodity avg `0.2856` n `12`; crypto_alt avg `-0.0212` n `232`; crypto_major avg `-1.0774` n `8`; equity avg `-0.1227` n `134`; fx avg `-0.1171` n `6`; index avg `-0.0461` n `26`; metal avg `0.1373` n `20`; unknown avg `7463.0178` n `670`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
