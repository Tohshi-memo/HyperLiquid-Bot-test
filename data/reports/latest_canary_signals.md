# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T07:22:28.819538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `0.2782` n `238`; crypto_major avg `0.1694` n `8`; equity avg `0.0794` n `154`; fx avg `0.0212` n `6`; index avg `0.0122` n `27`; metal avg `0.0468` n `20`; unknown avg `64.1412` n `1236`
- 1h: commodity avg `0.1697` n `13`; crypto_alt avg `0.2467` n `237`; crypto_major avg `0.0806` n `8`; equity avg `-0.1998` n `154`; fx avg `-0.0013` n `6`; index avg `-0.0096` n `27`; metal avg `-0.0321` n `20`; unknown avg `65.2353` n `1224`
- 4h: commodity avg `0.25` n `13`; crypto_alt avg `0.4444` n `237`; crypto_major avg `-0.053` n `8`; equity avg `-1.1507` n `154`; fx avg `-0.0372` n `6`; index avg `-0.0353` n `27`; metal avg `-0.1781` n `20`; unknown avg `75.3771` n `1190`
- 24h: commodity avg `0.1972` n `13`; crypto_alt avg `0.2246` n `237`; crypto_major avg `0.1073` n `8`; equity avg `0.4474` n `153`; fx avg `-0.0273` n `6`; index avg `0.0521` n `27`; metal avg `-0.2647` n `20`; unknown avg `1124.1442` n `980`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
