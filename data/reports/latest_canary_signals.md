# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T06:22:18.811893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0413` n `12`; crypto_alt avg `0.1597` n `228`; crypto_major avg `0.0334` n `8`; equity avg `-0.0352` n `66`; fx avg `0.0035` n `6`; index avg `-0.0154` n `23`; metal avg `0.072` n `18`; unknown avg `0.0061` n `385`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `-0.1351` n `228`; crypto_major avg `-0.0124` n `8`; equity avg `-0.2017` n `66`; fx avg `0.0215` n `6`; index avg `-0.0641` n `23`; metal avg `0.1245` n `18`; unknown avg `1.4274` n `374`
- 4h: commodity avg `0.0678` n `12`; crypto_alt avg `-0.3481` n `228`; crypto_major avg `0.046` n `8`; equity avg `0.076` n `66`; fx avg `0.0604` n `6`; index avg `0.104` n `23`; metal avg `-0.5301` n `18`; unknown avg `0.9978` n `374`
- 24h: commodity avg `-2.0574` n `12`; crypto_alt avg `2.3874` n `228`; crypto_major avg `2.936` n `8`; equity avg `2.0963` n `66`; fx avg `0.0767` n `6`; index avg `1.5193` n `23`; metal avg `0.7839` n `18`; unknown avg `5.8464` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
