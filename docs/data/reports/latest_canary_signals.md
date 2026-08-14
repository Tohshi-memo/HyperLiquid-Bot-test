# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T16:36:12.274801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.2002` n `230`; crypto_major avg `0.1073` n `8`; equity avg `-0.0474` n `114`; fx avg `0.0045` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0248` n `20`; unknown avg `18.7945` n `791`
- 1h: commodity avg `-0.026` n `12`; crypto_alt avg `0.6436` n `230`; crypto_major avg `0.1034` n `8`; equity avg `0.1376` n `114`; fx avg `0.0256` n `6`; index avg `0.0111` n `25`; metal avg `0.0411` n `20`; unknown avg `18.8023` n `791`
- 4h: commodity avg `0.1082` n `12`; crypto_alt avg `0.9137` n `230`; crypto_major avg `0.2752` n `8`; equity avg `-0.8528` n `114`; fx avg `0.1433` n `6`; index avg `-0.1624` n `25`; metal avg `0.084` n `20`; unknown avg `0.0027` n `786`
- 24h: commodity avg `-0.0804` n `12`; crypto_alt avg `0.5972` n `230`; crypto_major avg `-0.2856` n `8`; equity avg `-0.4154` n `114`; fx avg `0.1005` n `6`; index avg `-0.0897` n `25`; metal avg `0.1758` n `20`; unknown avg `0.3959` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
