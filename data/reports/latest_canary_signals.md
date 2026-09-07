# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T13:52:33.261760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `0.0197` n `232`; crypto_major avg `-0.0119` n `8`; equity avg `0.0233` n `134`; fx avg `-0.0074` n `6`; index avg `0.0017` n `26`; metal avg `0.0312` n `20`; unknown avg `-0.0614` n `796`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `-0.193` n `232`; crypto_major avg `-0.3173` n `8`; equity avg `0.0788` n `134`; fx avg `-0.0009` n `6`; index avg `0.0266` n `26`; metal avg `0.0499` n `20`; unknown avg `-0.3127` n `794`
- 4h: commodity avg `0.2458` n `12`; crypto_alt avg `0.9076` n `232`; crypto_major avg `0.3329` n `8`; equity avg `-0.0` n `134`; fx avg `0.0468` n `6`; index avg `-0.0113` n `26`; metal avg `-0.0297` n `20`; unknown avg `6684.0384` n `748`
- 24h: commodity avg `0.1817` n `12`; crypto_alt avg `0.7827` n `232`; crypto_major avg `-0.5827` n `8`; equity avg `0.3656` n `134`; fx avg `-0.103` n `6`; index avg `0.0286` n `26`; metal avg `-0.0931` n `20`; unknown avg `205.3981` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
