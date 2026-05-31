# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T05:37:18.552821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `0.0306` n `228`; crypto_major avg `-0.077` n `8`; equity avg `0.0335` n `69`; fx avg `0.0161` n `6`; index avg `0.0635` n `23`; metal avg `-0.0008` n `18`; unknown avg `0.8819` n `421`
- 1h: commodity avg `-0.0305` n `12`; crypto_alt avg `0.0556` n `228`; crypto_major avg `-0.0139` n `8`; equity avg `0.0856` n `69`; fx avg `-0.0051` n `6`; index avg `0.0695` n `23`; metal avg `0.0191` n `18`; unknown avg `0.4336` n `421`
- 4h: commodity avg `0.0198` n `12`; crypto_alt avg `0.3052` n `228`; crypto_major avg `0.2212` n `8`; equity avg `0.1513` n `69`; fx avg `0.032` n `6`; index avg `0.038` n `23`; metal avg `-0.0226` n `18`; unknown avg `0.1206` n `419`
- 24h: commodity avg `0.0717` n `12`; crypto_alt avg `0.7401` n `228`; crypto_major avg `2.46` n `8`; equity avg `0.9295` n `69`; fx avg `0.0459` n `6`; index avg `0.1187` n `23`; metal avg `0.0029` n `18`; unknown avg `0.6111` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
