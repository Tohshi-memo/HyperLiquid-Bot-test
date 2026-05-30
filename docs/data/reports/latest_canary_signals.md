# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T18:22:18.637920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0936` n `12`; crypto_alt avg `0.0352` n `228`; crypto_major avg `0.0392` n `8`; equity avg `0.004` n `69`; fx avg `0.0011` n `6`; index avg `-0.002` n `23`; metal avg `-0.0006` n `18`; unknown avg `0.1467` n `421`
- 1h: commodity avg `-0.1235` n `12`; crypto_alt avg `0.1051` n `228`; crypto_major avg `0.268` n `8`; equity avg `0.0013` n `69`; fx avg `-0.0013` n `6`; index avg `-0.0081` n `23`; metal avg `-0.0058` n `18`; unknown avg `-0.1185` n `421`
- 4h: commodity avg `-0.4926` n `12`; crypto_alt avg `0.2865` n `228`; crypto_major avg `0.8967` n `8`; equity avg `-0.1197` n `69`; fx avg `-0.0165` n `6`; index avg `-0.1371` n `23`; metal avg `0.0303` n `18`; unknown avg `0.1444` n `421`
- 24h: commodity avg `-0.0185` n `12`; crypto_alt avg `0.9361` n `228`; crypto_major avg `2.2627` n `8`; equity avg `0.8852` n `69`; fx avg `0.0044` n `6`; index avg `0.0789` n `23`; metal avg `-0.1122` n `18`; unknown avg `0.2863` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
