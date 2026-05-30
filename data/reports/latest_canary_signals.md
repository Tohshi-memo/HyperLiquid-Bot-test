# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T03:52:16.367938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0395` n `228`; crypto_major avg `-0.0342` n `8`; equity avg `-0.0188` n `69`; fx avg `-0.0012` n `6`; index avg `0.0251` n `23`; metal avg `-0.0011` n `18`; unknown avg `-0.0041` n `419`
- 1h: commodity avg `0.044` n `12`; crypto_alt avg `-0.4409` n `228`; crypto_major avg `-0.172` n `8`; equity avg `-0.0385` n `69`; fx avg `-0.0007` n `6`; index avg `0.0087` n `23`; metal avg `-0.0621` n `18`; unknown avg `-0.1229` n `419`
- 4h: commodity avg `-0.0725` n `12`; crypto_alt avg `1.2101` n `228`; crypto_major avg `1.0041` n `8`; equity avg `0.2446` n `69`; fx avg `0.003` n `6`; index avg `-0.0843` n `23`; metal avg `0.0117` n `18`; unknown avg `-0.6436` n `419`
- 24h: commodity avg `-0.3129` n `12`; crypto_alt avg `2.348` n `228`; crypto_major avg `2.2447` n `8`; equity avg `1.1172` n `69`; fx avg `0.0997` n `6`; index avg `0.1523` n `23`; metal avg `0.2045` n `18`; unknown avg `0.7029` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
