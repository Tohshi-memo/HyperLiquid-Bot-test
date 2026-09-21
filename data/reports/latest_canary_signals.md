# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T21:52:31.219570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `-0.4559` n `234`; crypto_major avg `-0.3279` n `8`; equity avg `-0.0117` n `140`; fx avg `0.0081` n `6`; index avg `0.0083` n `26`; metal avg `-0.023` n `20`; unknown avg `-0.0051` n `944`
- 1h: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.3514` n `234`; crypto_major avg `-0.2223` n `8`; equity avg `0.083` n `140`; fx avg `0.0072` n `6`; index avg `-0.0076` n `26`; metal avg `-0.024` n `20`; unknown avg `-0.2996` n `942`
- 4h: commodity avg `-0.0645` n `12`; crypto_alt avg `0.8127` n `234`; crypto_major avg `1.3768` n `8`; equity avg `0.2111` n `140`; fx avg `0.0081` n `6`; index avg `0.0098` n `26`; metal avg `0.0351` n `20`; unknown avg `36.8575` n `852`
- 24h: commodity avg `-1.0288` n `12`; crypto_alt avg `3.6946` n `234`; crypto_major avg `6.4061` n `8`; equity avg `2.8828` n `140`; fx avg `-0.0376` n `6`; index avg `0.594` n `26`; metal avg `0.0336` n `20`; unknown avg `11.3068` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
