# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T11:52:26.922676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `-0.0379` n `230`; crypto_major avg `0.0129` n `8`; equity avg `-0.1131` n `92`; fx avg `0.0133` n `6`; index avg `0.0077` n `25`; metal avg `-0.0396` n `20`; unknown avg `0.0135` n `766`
- 1h: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.0395` n `230`; crypto_major avg `0.1091` n `8`; equity avg `0.0892` n `92`; fx avg `0.0006` n `6`; index avg `0.0427` n `25`; metal avg `0.0535` n `20`; unknown avg `-0.0014` n `766`
- 4h: commodity avg `-0.0287` n `12`; crypto_alt avg `0.1131` n `230`; crypto_major avg `-0.0557` n `8`; equity avg `0.4962` n `92`; fx avg `-0.0502` n `6`; index avg `0.0834` n `25`; metal avg `0.1082` n `20`; unknown avg `-0.124` n `766`
- 24h: commodity avg `-0.1241` n `12`; crypto_alt avg `-1.1278` n `230`; crypto_major avg `-1.3971` n `8`; equity avg `-1.948` n `92`; fx avg `-0.0561` n `6`; index avg `-0.4144` n `25`; metal avg `-0.2198` n `20`; unknown avg `-0.1156` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
