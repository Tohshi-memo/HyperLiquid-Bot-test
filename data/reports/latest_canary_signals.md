# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T17:07:28.531855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0404` n `230`; crypto_major avg `-0.0487` n `8`; equity avg `-0.0096` n `92`; fx avg `0.0007` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0682` n `765`
- 1h: commodity avg `0.0877` n `12`; crypto_alt avg `-0.1427` n `230`; crypto_major avg `-0.0363` n `8`; equity avg `0.017` n `92`; fx avg `0.0215` n `6`; index avg `0.0071` n `25`; metal avg `-0.0093` n `20`; unknown avg `-0.066` n `759`
- 4h: commodity avg `0.0936` n `12`; crypto_alt avg `0.0092` n `230`; crypto_major avg `0.3161` n `8`; equity avg `-0.0172` n `92`; fx avg `0.0028` n `6`; index avg `0.0545` n `25`; metal avg `-0.0258` n `20`; unknown avg `-0.0082` n `759`
- 24h: commodity avg `0.5892` n `12`; crypto_alt avg `-1.1531` n `230`; crypto_major avg `-0.3295` n `8`; equity avg `-0.1323` n `92`; fx avg `0.0366` n `6`; index avg `-0.0863` n `25`; metal avg `-0.1027` n `20`; unknown avg `0.3784` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
