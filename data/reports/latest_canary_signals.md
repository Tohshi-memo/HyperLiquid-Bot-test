# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T15:07:25.589606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `0.1548` n `230`; crypto_major avg `0.159` n `8`; equity avg `0.0162` n `92`; fx avg `0.0` n `6`; index avg `0.0132` n `25`; metal avg `0.0096` n `20`; unknown avg `0.0097` n `765`
- 1h: commodity avg `-0.0233` n `12`; crypto_alt avg `0.4009` n `230`; crypto_major avg `0.4875` n `8`; equity avg `0.0217` n `92`; fx avg `-0.0051` n `6`; index avg `0.0126` n `25`; metal avg `0.0062` n `20`; unknown avg `0.0276` n `765`
- 4h: commodity avg `-0.1051` n `12`; crypto_alt avg `0.4644` n `230`; crypto_major avg `0.8758` n `8`; equity avg `0.1074` n `92`; fx avg `0.0012` n `6`; index avg `0.0376` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.0077` n `765`
- 24h: commodity avg `0.4472` n `12`; crypto_alt avg `-1.1094` n `230`; crypto_major avg `-0.4737` n `8`; equity avg `-0.0336` n `92`; fx avg `0.0194` n `6`; index avg `-0.0988` n `25`; metal avg `-0.0866` n `20`; unknown avg `0.1062` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
