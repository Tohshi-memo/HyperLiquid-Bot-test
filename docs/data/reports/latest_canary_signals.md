# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T11:04:22.479277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `-0.1552` n `228`; crypto_major avg `-0.0862` n `8`; equity avg `-0.0013` n `69`; fx avg `-0.0012` n `6`; index avg `0.0014` n `23`; metal avg `0.0056` n `18`; unknown avg `-0.0507` n `421`
- 1h: commodity avg `0.0734` n `12`; crypto_alt avg `-0.0255` n `228`; crypto_major avg `0.0764` n `8`; equity avg `0.038` n `69`; fx avg `-0.0008` n `6`; index avg `0.0219` n `23`; metal avg `0.0173` n `18`; unknown avg `0.0864` n `421`
- 4h: commodity avg `0.0451` n `12`; crypto_alt avg `0.1318` n `228`; crypto_major avg `0.2977` n `8`; equity avg `0.1219` n `69`; fx avg `0.022` n `6`; index avg `-0.0129` n `23`; metal avg `0.0401` n `18`; unknown avg `-0.0616` n `421`
- 24h: commodity avg `-0.2633` n `12`; crypto_alt avg `1.4556` n `228`; crypto_major avg `1.9958` n `8`; equity avg `1.2312` n `69`; fx avg `0.1032` n `6`; index avg `-0.0234` n `23`; metal avg `-0.1182` n `18`; unknown avg `0.4841` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
