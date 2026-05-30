# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T23:52:16.694044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0342` n `12`; crypto_alt avg `0.1757` n `228`; crypto_major avg `0.1436` n `8`; equity avg `0.0368` n `69`; fx avg `-0.0155` n `6`; index avg `0.0033` n `23`; metal avg `0.001` n `18`; unknown avg `-0.1456` n `421`
- 1h: commodity avg `-0.074` n `12`; crypto_alt avg `0.0631` n `228`; crypto_major avg `0.1311` n `8`; equity avg `0.0925` n `69`; fx avg `-0.0318` n `6`; index avg `-0.0238` n `23`; metal avg `-0.0096` n `18`; unknown avg `-0.3436` n `421`
- 4h: commodity avg `0.031` n `12`; crypto_alt avg `-0.6908` n `228`; crypto_major avg `-0.2409` n `8`; equity avg `0.2073` n `69`; fx avg `-0.0339` n `6`; index avg `-0.012` n `23`; metal avg `-0.0098` n `18`; unknown avg `-0.5119` n `421`
- 24h: commodity avg `-0.278` n `12`; crypto_alt avg `0.9217` n `228`; crypto_major avg `2.6036` n `8`; equity avg `1.0845` n `69`; fx avg `0.0082` n `6`; index avg `0.0447` n `23`; metal avg `0.0055` n `18`; unknown avg `0.1296` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
