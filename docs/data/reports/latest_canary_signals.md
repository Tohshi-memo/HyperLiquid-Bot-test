# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T10:52:29.133339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `13`; crypto_alt avg `0.0101` n `239`; crypto_major avg `-0.0539` n `8`; equity avg `-0.0495` n `157`; fx avg `-0.0077` n `6`; index avg `-0.0098` n `27`; metal avg `0.0145` n `20`; unknown avg `0.1653` n `1260`
- 1h: commodity avg `0.0702` n `13`; crypto_alt avg `0.2076` n `239`; crypto_major avg `0.0431` n `8`; equity avg `0.0749` n `157`; fx avg `-0.015` n `6`; index avg `0.0057` n `27`; metal avg `0.0014` n `20`; unknown avg `-0.0548` n `1256`
- 4h: commodity avg `0.1355` n `13`; crypto_alt avg `1.0058` n `239`; crypto_major avg `0.7469` n `8`; equity avg `1.0387` n `157`; fx avg `0.0708` n `6`; index avg `0.1093` n `27`; metal avg `-0.1059` n `20`; unknown avg `0.7789` n `1226`
- 24h: commodity avg `-0.321` n `13`; crypto_alt avg `-1.5758` n `238`; crypto_major avg `-1.0109` n `8`; equity avg `-3.4535` n `157`; fx avg `0.0268` n `6`; index avg `-0.2224` n `27`; metal avg `-0.4638` n `20`; unknown avg `42.7717` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
