# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T00:22:25.601925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `0.2969` n `228`; crypto_major avg `0.2231` n `8`; equity avg `-0.0294` n `69`; fx avg `0.0013` n `6`; index avg `-0.0195` n `23`; metal avg `-0.0038` n `18`; unknown avg `-0.205` n `421`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.3934` n `228`; crypto_major avg `0.4307` n `8`; equity avg `-0.0168` n `69`; fx avg `0.0081` n `6`; index avg `-0.0199` n `23`; metal avg `0.0032` n `18`; unknown avg `-0.1693` n `421`
- 4h: commodity avg `0.1342` n `12`; crypto_alt avg `-0.509` n `228`; crypto_major avg `0.0866` n `8`; equity avg `0.1754` n `69`; fx avg `-0.0109` n `6`; index avg `0.0208` n `23`; metal avg `-0.0179` n `18`; unknown avg `0.4947` n `421`
- 24h: commodity avg `-0.2908` n `12`; crypto_alt avg `1.0745` n `228`; crypto_major avg `2.7872` n `8`; equity avg `1.1198` n `69`; fx avg `0.0321` n `6`; index avg `0.0237` n `23`; metal avg `-0.005` n `18`; unknown avg `1.2` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
