# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T18:07:26.198025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `13`; crypto_alt avg `0.1349` n `239`; crypto_major avg `0.1394` n `8`; equity avg `0.0231` n `162`; fx avg `0.0054` n `6`; index avg `0.0056` n `27`; metal avg `0.0118` n `20`; unknown avg `1.6285` n `1259`
- 1h: commodity avg `-0.0092` n `13`; crypto_alt avg `-0.0058` n `239`; crypto_major avg `0.0129` n `8`; equity avg `-0.1348` n `162`; fx avg `0.0087` n `6`; index avg `-0.0068` n `27`; metal avg `0.0239` n `20`; unknown avg `3.326` n `1263`
- 4h: commodity avg `0.0213` n `13`; crypto_alt avg `-0.6227` n `239`; crypto_major avg `-0.6914` n `8`; equity avg `0.0518` n `162`; fx avg `0.0078` n `6`; index avg `0.0204` n `27`; metal avg `0.0272` n `20`; unknown avg `2.5639` n `1256`
- 24h: commodity avg `0.015` n `13`; crypto_alt avg `-1.2026` n `239`; crypto_major avg `-0.7608` n `8`; equity avg `0.1574` n `162`; fx avg `-0.0073` n `6`; index avg `0.041` n `27`; metal avg `-0.1243` n `20`; unknown avg `2.4835` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
