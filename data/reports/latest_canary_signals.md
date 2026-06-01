# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T23:37:19.229174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0463` n `12`; crypto_alt avg `0.0319` n `228`; crypto_major avg `-0.1499` n `8`; equity avg `0.0276` n `69`; fx avg `0.0061` n `6`; index avg `-0.0118` n `23`; metal avg `-0.0478` n `18`; unknown avg `-0.065` n `422`
- 1h: commodity avg `-0.1789` n `12`; crypto_alt avg `0.8717` n `228`; crypto_major avg `0.7018` n `8`; equity avg `0.1014` n `69`; fx avg `0.0073` n `6`; index avg `0.0296` n `23`; metal avg `0.0755` n `18`; unknown avg `0.5089` n `422`
- 4h: commodity avg `0.0319` n `12`; crypto_alt avg `-0.2146` n `228`; crypto_major avg `0.1478` n `8`; equity avg `-0.1976` n `69`; fx avg `-0.0153` n `6`; index avg `-0.3086` n `23`; metal avg `-0.0447` n `18`; unknown avg `-0.1545` n `422`
- 24h: commodity avg `0.1248` n `12`; crypto_alt avg `0.6424` n `228`; crypto_major avg `-0.4136` n `8`; equity avg `-0.1306` n `69`; fx avg `0.0444` n `6`; index avg `0.2343` n `23`; metal avg `-0.331` n `18`; unknown avg `1.7104` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
