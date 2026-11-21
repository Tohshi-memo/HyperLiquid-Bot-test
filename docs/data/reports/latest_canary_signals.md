# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T19:07:29.501392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `-0.0327` n `239`; crypto_major avg `0.2287` n `8`; equity avg `0.0349` n `166`; fx avg `0.0001` n `6`; index avg `0.0119` n `27`; metal avg `-0.0542` n `20`; unknown avg `40.2081` n `1254`
- 1h: commodity avg `0.0237` n `13`; crypto_alt avg `-0.088` n `239`; crypto_major avg `0.2127` n `8`; equity avg `0.0576` n `166`; fx avg `0.0167` n `6`; index avg `0.1025` n `27`; metal avg `0.0193` n `20`; unknown avg `40.3554` n `1256`
- 4h: commodity avg `0.0273` n `13`; crypto_alt avg `-0.536` n `239`; crypto_major avg `0.0118` n `8`; equity avg `0.0335` n `166`; fx avg `0.0142` n `6`; index avg `0.027` n `27`; metal avg `0.0158` n `20`; unknown avg `166.3545` n `1200`
- 24h: commodity avg `0.2754` n `13`; crypto_alt avg `0.8499` n `239`; crypto_major avg `2.5431` n `8`; equity avg `0.1257` n `166`; fx avg `-0.0859` n `6`; index avg `0.0304` n `27`; metal avg `0.1453` n `20`; unknown avg `183.2297` n `1094`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
