# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T22:41:59.209224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0545` n `12`; crypto_alt avg `-0.1412` n `228`; crypto_major avg `-0.154` n `8`; equity avg `0.0102` n `69`; fx avg `-0.0018` n `6`; index avg `0.0235` n `23`; metal avg `0.0055` n `18`; unknown avg `-0.2443` n `419`
- 1h: commodity avg `0.1458` n `12`; crypto_alt avg `-0.0327` n `228`; crypto_major avg `-0.0147` n `8`; equity avg `-0.0361` n `69`; fx avg `0.002` n `6`; index avg `0.0945` n `23`; metal avg `0.0681` n `18`; unknown avg `0.0265` n `419`
- 4h: commodity avg `0.3115` n `12`; crypto_alt avg `-0.7188` n `228`; crypto_major avg `-0.6224` n `8`; equity avg `0.1701` n `69`; fx avg `-0.0273` n `6`; index avg `0.0572` n `23`; metal avg `-0.2285` n `18`; unknown avg `-0.2547` n `419`
- 24h: commodity avg `-0.5776` n `12`; crypto_alt avg `0.7465` n `228`; crypto_major avg `0.8463` n `8`; equity avg `1.0289` n `69`; fx avg `0.183` n `6`; index avg `0.1709` n `23`; metal avg `0.0768` n `18`; unknown avg `0.4372` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
