# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T08:37:27.700644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `-0.0739` n `238`; crypto_major avg `-0.2807` n `8`; equity avg `-0.0371` n `156`; fx avg `0.0007` n `6`; index avg `0.0032` n `27`; metal avg `-0.0108` n `20`; unknown avg `0.1555` n `1262`
- 1h: commodity avg `0.0132` n `13`; crypto_alt avg `-0.1853` n `238`; crypto_major avg `-0.3949` n `8`; equity avg `-0.0867` n `156`; fx avg `0.0077` n `6`; index avg `-0.0008` n `27`; metal avg `-0.0253` n `20`; unknown avg `202.1453` n `1238`
- 4h: commodity avg `-0.0255` n `13`; crypto_alt avg `-0.6066` n `238`; crypto_major avg `-0.5134` n `8`; equity avg `-0.0727` n `156`; fx avg `0.0139` n `6`; index avg `0.0085` n `27`; metal avg `-0.0156` n `20`; unknown avg `0.8187` n `1210`
- 24h: commodity avg `-0.2175` n `13`; crypto_alt avg `0.5219` n `238`; crypto_major avg `-1.3838` n `8`; equity avg `-2.0187` n `156`; fx avg `-0.059` n `6`; index avg `-0.187` n `27`; metal avg `-0.4364` n `20`; unknown avg `4.5278` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
