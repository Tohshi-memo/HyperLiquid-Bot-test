# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T02:22:27.911150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `13`; crypto_alt avg `-0.3077` n `239`; crypto_major avg `-0.3867` n `8`; equity avg `-0.1794` n `166`; fx avg `0.0` n `6`; index avg `-0.0371` n `27`; metal avg `-0.0316` n `20`; unknown avg `0.6572` n `1261`
- 1h: commodity avg `-0.0467` n `13`; crypto_alt avg `-0.3351` n `239`; crypto_major avg `-0.5069` n `8`; equity avg `-0.248` n `166`; fx avg `-0.007` n `6`; index avg `-0.0303` n `27`; metal avg `-0.0381` n `20`; unknown avg `2.6115` n `1261`
- 4h: commodity avg `-0.0117` n `13`; crypto_alt avg `-0.3218` n `239`; crypto_major avg `-0.429` n `8`; equity avg `-0.1847` n `166`; fx avg `-0.0094` n `6`; index avg `0.001` n `27`; metal avg `-0.014` n `20`; unknown avg `163.8306` n `1244`
- 24h: commodity avg `0.0197` n `13`; crypto_alt avg `-0.1688` n `239`; crypto_major avg `1.4426` n `8`; equity avg `0.5092` n `166`; fx avg `-0.0434` n `6`; index avg `0.1511` n `27`; metal avg `0.0861` n `20`; unknown avg `232.7114` n `1082`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
