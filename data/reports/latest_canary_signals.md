# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T09:37:37.660682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.0758` n `230`; crypto_major avg `0.039` n `8`; equity avg `0.0022` n `114`; fx avg `-0.0021` n `6`; index avg `-0.0112` n `25`; metal avg `0.0025` n `20`; unknown avg `0.0164` n `791`
- 1h: commodity avg `-0.0103` n `12`; crypto_alt avg `0.008` n `230`; crypto_major avg `-0.0137` n `8`; equity avg `-0.027` n `114`; fx avg `0.0001` n `6`; index avg `0.0005` n `25`; metal avg `0.0044` n `20`; unknown avg `-0.0089` n `791`
- 4h: commodity avg `-0.1955` n `12`; crypto_alt avg `-0.1249` n `230`; crypto_major avg `-0.0528` n `8`; equity avg `0.0012` n `114`; fx avg `-0.0052` n `6`; index avg `-0.0008` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0111` n `759`
- 24h: commodity avg `-0.1241` n `12`; crypto_alt avg `1.0626` n `230`; crypto_major avg `0.0705` n `8`; equity avg `-0.3915` n `114`; fx avg `0.1586` n `6`; index avg `-0.1095` n `25`; metal avg `0.1846` n `20`; unknown avg `-0.0819` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
