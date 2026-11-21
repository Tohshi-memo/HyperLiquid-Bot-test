# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T23:22:25.245783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `0.1185` n `239`; crypto_major avg `0.1863` n `8`; equity avg `0.0419` n `166`; fx avg `0.0009` n `6`; index avg `0.0375` n `27`; metal avg `-0.0003` n `20`; unknown avg `0.2071` n `1256`
- 1h: commodity avg `0.0011` n `13`; crypto_alt avg `0.1193` n `239`; crypto_major avg `0.0354` n `8`; equity avg `-0.066` n `166`; fx avg `0.0142` n `6`; index avg `0.0309` n `27`; metal avg `0.0056` n `20`; unknown avg `162.5172` n `1244`
- 4h: commodity avg `0.0088` n `13`; crypto_alt avg `0.0855` n `239`; crypto_major avg `-0.0598` n `8`; equity avg `0.1453` n `166`; fx avg `0.019` n `6`; index avg `0.091` n `27`; metal avg `-0.0664` n `20`; unknown avg `207.3304` n `1202`
- 24h: commodity avg `0.0077` n `13`; crypto_alt avg `-0.0593` n `239`; crypto_major avg `1.5862` n `8`; equity avg `0.2609` n `166`; fx avg `-0.025` n `6`; index avg `0.1469` n `27`; metal avg `0.0904` n `20`; unknown avg `601.9991` n `1082`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
