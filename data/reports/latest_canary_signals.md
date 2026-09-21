# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T14:21:34.786525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0951` n `12`; crypto_alt avg `0.3689` n `234`; crypto_major avg `0.3254` n `8`; equity avg `0.1614` n `140`; fx avg `-0.0069` n `6`; index avg `0.0579` n `26`; metal avg `0.0298` n `20`; unknown avg `2.3414` n `944`
- 1h: commodity avg `-0.0926` n `12`; crypto_alt avg `-0.5163` n `234`; crypto_major avg `-0.2541` n `8`; equity avg `0.277` n `140`; fx avg `-0.0208` n `6`; index avg `0.0956` n `26`; metal avg `-0.2051` n `20`; unknown avg `10.5956` n `898`
- 4h: commodity avg `-0.2394` n `12`; crypto_alt avg `0.1965` n `234`; crypto_major avg `0.5919` n `8`; equity avg `0.3198` n `140`; fx avg `0.0055` n `6`; index avg `0.1053` n `26`; metal avg `0.0408` n `20`; unknown avg `11.2727` n `868`
- 24h: commodity avg `-0.9879` n `12`; crypto_alt avg `6.8978` n `234`; crypto_major avg `6.0609` n `8`; equity avg `2.381` n `140`; fx avg `-0.081` n `6`; index avg `0.4613` n `26`; metal avg `0.0777` n `20`; unknown avg `3.194` n `711`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
