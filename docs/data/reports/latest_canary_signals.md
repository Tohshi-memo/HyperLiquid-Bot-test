# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T06:07:27.729779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0156` n `12`; crypto_alt avg `-0.1468` n `234`; crypto_major avg `-0.1644` n `8`; equity avg `-0.0382` n `140`; fx avg `-0.0178` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0033` n `20`; unknown avg `0.0327` n `904`
- 1h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.6119` n `234`; crypto_major avg `-0.1222` n `8`; equity avg `-0.0724` n `140`; fx avg `0.0029` n `6`; index avg `-0.0395` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.0361` n `904`
- 4h: commodity avg `-0.0473` n `12`; crypto_alt avg `-0.7914` n `234`; crypto_major avg `-0.3013` n `8`; equity avg `-0.0949` n `140`; fx avg `-0.0088` n `6`; index avg `-0.0433` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.4066` n `894`
- 24h: commodity avg `0.1425` n `12`; crypto_alt avg `3.3192` n `234`; crypto_major avg `4.3633` n `8`; equity avg `0.2944` n `140`; fx avg `0.0696` n `6`; index avg `-0.0438` n `26`; metal avg `-0.1185` n `20`; unknown avg `2.2318` n `785`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
