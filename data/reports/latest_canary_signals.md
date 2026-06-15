# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T19:07:44.352897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `0.0293` n `228`; crypto_major avg `0.1102` n `8`; equity avg `-0.1791` n `77`; fx avg `-0.019` n `6`; index avg `-0.0516` n `23`; metal avg `-0.1097` n `18`; unknown avg `0.0038` n `687`
- 1h: commodity avg `0.2143` n `12`; crypto_alt avg `-0.2954` n `228`; crypto_major avg `0.0962` n `8`; equity avg `-0.1471` n `77`; fx avg `-0.0201` n `6`; index avg `-0.0249` n `23`; metal avg `0.0569` n `18`; unknown avg `0.0086` n `687`
- 4h: commodity avg `0.3227` n `12`; crypto_alt avg `-0.4132` n `228`; crypto_major avg `0.8411` n `8`; equity avg `0.4557` n `77`; fx avg `-0.0176` n `6`; index avg `0.0915` n `23`; metal avg `-0.6273` n `18`; unknown avg `3.4635` n `687`
- 24h: commodity avg `-0.7362` n `12`; crypto_alt avg `5.9118` n `228`; crypto_major avg `7.5687` n `8`; equity avg `2.8818` n `76`; fx avg `0.0656` n `6`; index avg `1.2339` n `23`; metal avg `2.1147` n `18`; unknown avg `5.5818` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
