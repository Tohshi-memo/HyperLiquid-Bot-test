# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T22:52:26.642468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.0458` n `228`; crypto_major avg `-0.0997` n `8`; equity avg `-0.0167` n `69`; fx avg `0.0031` n `6`; index avg `-0.0305` n `23`; metal avg `0.0053` n `18`; unknown avg `0.0076` n `419`
- 1h: commodity avg `0.1354` n `12`; crypto_alt avg `-0.0831` n `228`; crypto_major avg `-0.054` n `8`; equity avg `0.0473` n `69`; fx avg `0.007` n `6`; index avg `-0.0098` n `23`; metal avg `0.0688` n `18`; unknown avg `-0.1182` n `419`
- 4h: commodity avg `0.0912` n `12`; crypto_alt avg `-0.0618` n `228`; crypto_major avg `-0.0502` n `8`; equity avg `0.447` n `69`; fx avg `-0.0195` n `6`; index avg `0.097` n `23`; metal avg `-0.1053` n `18`; unknown avg `-0.3526` n `419`
- 24h: commodity avg `-0.5244` n `12`; crypto_alt avg `0.5628` n `228`; crypto_major avg `0.6238` n `8`; equity avg `0.9143` n `69`; fx avg `0.1879` n `6`; index avg `0.1317` n `23`; metal avg `0.0897` n `18`; unknown avg `0.4149` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
