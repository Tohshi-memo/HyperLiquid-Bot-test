# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T13:52:28.971214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0562` n `13`; crypto_alt avg `-0.0397` n `239`; crypto_major avg `0.1283` n `8`; equity avg `0.0226` n `164`; fx avg `-0.0047` n `6`; index avg `0.0077` n `27`; metal avg `-0.0166` n `20`; unknown avg `0.3744` n `1266`
- 1h: commodity avg `0.0692` n `13`; crypto_alt avg `0.056` n `239`; crypto_major avg `0.0979` n `8`; equity avg `-0.4813` n `164`; fx avg `-0.0011` n `6`; index avg `-0.0555` n `27`; metal avg `-0.0539` n `20`; unknown avg `1.2265` n `1264`
- 4h: commodity avg `0.2067` n `13`; crypto_alt avg `0.008` n `239`; crypto_major avg `0.2709` n `8`; equity avg `-0.1907` n `164`; fx avg `-0.0107` n `6`; index avg `-0.0671` n `27`; metal avg `-0.1788` n `20`; unknown avg `10.0843` n `1258`
- 24h: commodity avg `0.0335` n `13`; crypto_alt avg `0.3692` n `239`; crypto_major avg `0.584` n `8`; equity avg `0.6796` n `164`; fx avg `0.0119` n `6`; index avg `0.2588` n `27`; metal avg `-0.3658` n `20`; unknown avg `2.0691` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
