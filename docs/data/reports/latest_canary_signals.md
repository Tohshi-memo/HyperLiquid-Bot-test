# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T13:37:27.311209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0383` n `12`; crypto_alt avg `-0.4217` n `232`; crypto_major avg `-0.451` n `8`; equity avg `-0.0327` n `134`; fx avg `0.0081` n `6`; index avg `-0.0028` n `26`; metal avg `0.0095` n `20`; unknown avg `-0.1122` n `796`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.1846` n `232`; crypto_major avg `-0.1097` n `8`; equity avg `0.0696` n `134`; fx avg `0.0158` n `6`; index avg `0.0335` n `26`; metal avg `0.0204` n `20`; unknown avg `-0.2445` n `794`
- 4h: commodity avg `0.246` n `12`; crypto_alt avg `0.8051` n `232`; crypto_major avg `0.2652` n `8`; equity avg `-0.0302` n `134`; fx avg `0.0575` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0639` n `20`; unknown avg `6683.9377` n `748`
- 24h: commodity avg `0.1897` n `12`; crypto_alt avg `0.9235` n `232`; crypto_major avg `-0.3849` n `8`; equity avg `0.3534` n `134`; fx avg `-0.0918` n `6`; index avg `0.0299` n `26`; metal avg `-0.1248` n `20`; unknown avg `209.7622` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
