# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T03:07:30.385727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0548` n `12`; crypto_alt avg `0.0746` n `230`; crypto_major avg `0.2627` n `8`; equity avg `-0.0242` n `93`; fx avg `0.0109` n `6`; index avg `0.0098` n `25`; metal avg `0.006` n `20`; unknown avg `-0.035` n `767`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.1419` n `230`; crypto_major avg `0.3368` n `8`; equity avg `0.2966` n `93`; fx avg `0.0152` n `6`; index avg `0.0198` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.2115` n `767`
- 4h: commodity avg `0.0663` n `12`; crypto_alt avg `-0.1735` n `230`; crypto_major avg `-0.0959` n `8`; equity avg `1.1548` n `93`; fx avg `0.0748` n `6`; index avg `0.1498` n `25`; metal avg `0.0322` n `20`; unknown avg `-0.5381` n `765`
- 24h: commodity avg `0.1319` n `12`; crypto_alt avg `1.8605` n `230`; crypto_major avg `3.264` n `8`; equity avg `2.9577` n `92`; fx avg `0.1266` n `6`; index avg `0.8265` n `25`; metal avg `0.4949` n `20`; unknown avg `0.2444` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0432`, n `668`, weak_sample_signal
