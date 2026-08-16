# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T15:07:27.757946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `0.0029` n `230`; crypto_major avg `0.0283` n `8`; equity avg `0.0037` n `114`; fx avg `-0.0018` n `6`; index avg `0.0008` n `25`; metal avg `-0.01` n `20`; unknown avg `0.0035` n `791`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.0212` n `230`; crypto_major avg `0.0776` n `8`; equity avg `0.0418` n `114`; fx avg `-0.0026` n `6`; index avg `-0.0112` n `25`; metal avg `-0.0147` n `20`; unknown avg `-0.0139` n `791`
- 4h: commodity avg `-0.0147` n `12`; crypto_alt avg `0.0821` n `230`; crypto_major avg `0.0955` n `8`; equity avg `-0.0324` n `114`; fx avg `-0.0167` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0103` n `20`; unknown avg `0.111` n `791`
- 24h: commodity avg `0.0554` n `12`; crypto_alt avg `-0.1213` n `230`; crypto_major avg `0.1153` n `8`; equity avg `0.2644` n `114`; fx avg `-0.0163` n `6`; index avg `0.0288` n `25`; metal avg `0.0281` n `20`; unknown avg `0.1621` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
