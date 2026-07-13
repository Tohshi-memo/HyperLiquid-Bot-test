# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T08:22:30.297903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.033` n `12`; crypto_alt avg `-0.1216` n `230`; crypto_major avg `-0.0518` n `8`; equity avg `0.1899` n `92`; fx avg `0.0226` n `6`; index avg `0.0398` n `25`; metal avg `0.0672` n `20`; unknown avg `0.076` n `766`
- 1h: commodity avg `-0.1889` n `12`; crypto_alt avg `0.1239` n `230`; crypto_major avg `0.11` n `8`; equity avg `0.2294` n `92`; fx avg `-0.0092` n `6`; index avg `0.0618` n `25`; metal avg `0.2323` n `20`; unknown avg `0.0969` n `766`
- 4h: commodity avg `-0.2301` n `12`; crypto_alt avg `0.5254` n `230`; crypto_major avg `-0.0507` n `8`; equity avg `0.2075` n `92`; fx avg `-0.029` n `6`; index avg `0.078` n `25`; metal avg `0.3435` n `20`; unknown avg `-0.0107` n `750`
- 24h: commodity avg `-0.1638` n `12`; crypto_alt avg `-1.2294` n `230`; crypto_major avg `-1.0741` n `8`; equity avg `-2.0526` n `92`; fx avg `-0.0007` n `6`; index avg `-0.4223` n `25`; metal avg `-0.1245` n `20`; unknown avg `-0.0406` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
