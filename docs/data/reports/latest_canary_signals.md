# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T09:17:59.901584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.131` n `230`; crypto_major avg `0.0682` n `8`; equity avg `0.0085` n `114`; fx avg `0.0025` n `6`; index avg `0.0051` n `25`; metal avg `0.0038` n `20`; unknown avg `0.0483` n `791`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `0.1122` n `230`; crypto_major avg `-0.1353` n `8`; equity avg `-0.0192` n `114`; fx avg `-0.0089` n `6`; index avg `0.0083` n `25`; metal avg `0.0014` n `20`; unknown avg `0.0589` n `791`
- 4h: commodity avg `-0.1904` n `12`; crypto_alt avg `-0.0613` n `230`; crypto_major avg `-0.2485` n `8`; equity avg `-0.0309` n `114`; fx avg `-0.0062` n `6`; index avg `0.0008` n `25`; metal avg `0.0093` n `20`; unknown avg `0.0577` n `759`
- 24h: commodity avg `-0.1243` n `12`; crypto_alt avg `0.941` n `230`; crypto_major avg `-0.1675` n `8`; equity avg `-0.4154` n `114`; fx avg `0.1617` n `6`; index avg `-0.1053` n `25`; metal avg `0.2024` n `20`; unknown avg `-0.0864` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
