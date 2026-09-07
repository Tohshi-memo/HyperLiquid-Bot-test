# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T10:22:30.922341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `-0.0142` n `232`; crypto_major avg `0.0432` n `8`; equity avg `0.0448` n `134`; fx avg `0.0189` n `6`; index avg `0.0045` n `26`; metal avg `-0.0061` n `20`; unknown avg `-0.1424` n `796`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `-0.2462` n `232`; crypto_major avg `-0.1494` n `8`; equity avg `0.0064` n `134`; fx avg `0.0276` n `6`; index avg `0.0016` n `26`; metal avg `-0.0443` n `20`; unknown avg `0.5932` n `794`
- 4h: commodity avg `-0.1589` n `12`; crypto_alt avg `-0.0339` n `232`; crypto_major avg `-0.2849` n `8`; equity avg `-0.0103` n `134`; fx avg `-0.0413` n `6`; index avg `0.0185` n `26`; metal avg `0.0633` n `20`; unknown avg `2.2376` n `774`
- 24h: commodity avg `-0.0691` n `12`; crypto_alt avg `0.1054` n `232`; crypto_major avg `-0.7977` n `8`; equity avg `0.3298` n `134`; fx avg `-0.1151` n `6`; index avg `0.021` n `26`; metal avg `-0.1204` n `20`; unknown avg `230.1499` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
