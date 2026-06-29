# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T16:37:29.600434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0235` n `12`; crypto_alt avg `-0.0518` n `228`; crypto_major avg `-0.0006` n `8`; equity avg `0.009` n `88`; fx avg `-0.0022` n `6`; index avg `-0.0174` n `23`; metal avg `-0.0921` n `20`; unknown avg `0.0456` n `765`
- 1h: commodity avg `0.0919` n `12`; crypto_alt avg `-0.1425` n `228`; crypto_major avg `-0.3926` n `8`; equity avg `0.4968` n `88`; fx avg `-0.0058` n `6`; index avg `0.0678` n `23`; metal avg `-0.1646` n `20`; unknown avg `0.6891` n `765`
- 4h: commodity avg `0.1402` n `12`; crypto_alt avg `-0.6275` n `228`; crypto_major avg `-0.6245` n `8`; equity avg `0.0601` n `88`; fx avg `0.0276` n `6`; index avg `-0.0057` n `23`; metal avg `-0.4098` n `20`; unknown avg `0.5185` n `764`
- 24h: commodity avg `-0.5526` n `12`; crypto_alt avg `0.5764` n `228`; crypto_major avg `0.7131` n `8`; equity avg `0.7364` n `88`; fx avg `0.1235` n `6`; index avg `0.0661` n `23`; metal avg `-0.6951` n `20`; unknown avg `1.5205` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
