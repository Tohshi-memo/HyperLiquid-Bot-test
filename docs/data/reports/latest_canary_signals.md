# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T11:52:43.645478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1462` n `12`; crypto_alt avg `0.2316` n `233`; crypto_major avg `0.3556` n `8`; equity avg `0.1599` n `134`; fx avg `-0.0076` n `6`; index avg `0.0287` n `26`; metal avg `0.067` n `20`; unknown avg `-0.0277` n `798`
- 1h: commodity avg `-0.0499` n `12`; crypto_alt avg `0.4744` n `233`; crypto_major avg `0.4058` n `8`; equity avg `0.1788` n `134`; fx avg `0.0011` n `6`; index avg `0.0398` n `26`; metal avg `0.0596` n `20`; unknown avg `0.0788` n `796`
- 4h: commodity avg `0.0169` n `12`; crypto_alt avg `-0.2495` n `233`; crypto_major avg `-0.3005` n `8`; equity avg `-0.5093` n `134`; fx avg `0.0299` n `6`; index avg `-0.1422` n `26`; metal avg `-0.086` n `20`; unknown avg `13.5676` n `790`
- 24h: commodity avg `-0.1791` n `12`; crypto_alt avg `0.5231` n `232`; crypto_major avg `1.462` n `8`; equity avg `0.5161` n `134`; fx avg `-0.108` n `6`; index avg `-0.1205` n `26`; metal avg `0.029` n `20`; unknown avg `0.9445` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
