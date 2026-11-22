# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T02:07:27.900226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `-0.1835` n `239`; crypto_major avg `-0.1663` n `8`; equity avg `-0.0595` n `166`; fx avg `0.0002` n `6`; index avg `0.0015` n `27`; metal avg `-0.0022` n `20`; unknown avg `-0.0239` n `1255`
- 1h: commodity avg `-0.0055` n `13`; crypto_alt avg `-0.0942` n `239`; crypto_major avg `-0.1074` n `8`; equity avg `-0.0695` n `166`; fx avg `0.0132` n `6`; index avg `0.0095` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.0746` n `1261`
- 4h: commodity avg `-0.0017` n `13`; crypto_alt avg `0.1872` n `239`; crypto_major avg `0.1274` n `8`; equity avg `0.0999` n `166`; fx avg `-0.0051` n `6`; index avg `0.0479` n `27`; metal avg `0.0055` n `20`; unknown avg `162.1139` n `1236`
- 24h: commodity avg `0.0501` n `13`; crypto_alt avg `0.3652` n `239`; crypto_major avg `1.8371` n `8`; equity avg `0.6086` n `166`; fx avg `-0.0522` n `6`; index avg `0.1821` n `27`; metal avg `0.1305` n `20`; unknown avg `232.5845` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
