# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T00:07:23.365517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0776` n `12`; crypto_alt avg `0.0904` n `228`; crypto_major avg `0.0238` n `8`; equity avg `-0.0909` n `69`; fx avg `0.0008` n `6`; index avg `-0.0155` n `23`; metal avg `0.0023` n `18`; unknown avg `0.2638` n `419`
- 1h: commodity avg `0.1169` n `12`; crypto_alt avg `0.0873` n `228`; crypto_major avg `-0.0023` n `8`; equity avg `-0.0542` n `69`; fx avg `-0.0106` n `6`; index avg `0.0732` n `23`; metal avg `0.0108` n `18`; unknown avg `0.8922` n `419`
- 4h: commodity avg `0.3221` n `12`; crypto_alt avg `-0.032` n `228`; crypto_major avg `-0.2863` n `8`; equity avg `-0.15` n `69`; fx avg `-0.0603` n `6`; index avg `-0.0022` n `23`; metal avg `-0.0565` n `18`; unknown avg `-0.0909` n `419`
- 24h: commodity avg `-0.1354` n `12`; crypto_alt avg `0.5731` n `228`; crypto_major avg `0.8266` n `8`; equity avg `0.7452` n `69`; fx avg `0.1235` n `6`; index avg `0.1714` n `23`; metal avg `0.0452` n `18`; unknown avg `1.559` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
