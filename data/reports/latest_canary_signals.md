# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T04:22:26.614853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.5218` n `231`; crypto_major avg `0.3535` n `8`; equity avg `0.0976` n `122`; fx avg `0.0013` n `6`; index avg `0.0093` n `25`; metal avg `0.0052` n `20`; unknown avg `-0.0712` n `793`
- 1h: commodity avg `-0.0102` n `12`; crypto_alt avg `0.5808` n `231`; crypto_major avg `0.3369` n `8`; equity avg `-0.0541` n `122`; fx avg `0.0132` n `6`; index avg `-0.011` n `25`; metal avg `-0.0285` n `20`; unknown avg `-0.1557` n `793`
- 4h: commodity avg `-0.0459` n `12`; crypto_alt avg `-0.6257` n `231`; crypto_major avg `-0.6451` n `8`; equity avg `-1.2132` n `122`; fx avg `-0.0254` n `6`; index avg `-0.1088` n `25`; metal avg `0.0012` n `20`; unknown avg `0.3098` n `793`
- 24h: commodity avg `-0.2917` n `12`; crypto_alt avg `4.108` n `231`; crypto_major avg `1.1617` n `8`; equity avg `-1.0319` n `122`; fx avg `-0.1832` n `6`; index avg `-0.0983` n `25`; metal avg `0.106` n `20`; unknown avg `6.0536` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
