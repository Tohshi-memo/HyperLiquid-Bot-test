# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T08:52:35.002647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.0466` n `228`; crypto_major avg `0.0799` n `8`; equity avg `-0.0224` n `88`; fx avg `-0.0101` n `6`; index avg `0.0038` n `23`; metal avg `-0.0937` n `20`; unknown avg `-0.0293` n `764`
- 1h: commodity avg `0.0798` n `12`; crypto_alt avg `-0.2416` n `228`; crypto_major avg `-0.2025` n `8`; equity avg `0.1266` n `88`; fx avg `-0.0081` n `6`; index avg `0.0043` n `23`; metal avg `-0.1223` n `20`; unknown avg `1.192` n `764`
- 4h: commodity avg `-0.1277` n `12`; crypto_alt avg `0.3878` n `228`; crypto_major avg `0.4994` n `8`; equity avg `0.8153` n `88`; fx avg `0.0164` n `6`; index avg `0.2441` n `23`; metal avg `0.0867` n `20`; unknown avg `1.9066` n `732`
- 24h: commodity avg `-0.4279` n `12`; crypto_alt avg `-0.2005` n `228`; crypto_major avg `-0.5443` n `8`; equity avg `0.4196` n `88`; fx avg `0.059` n `6`; index avg `0.0807` n `23`; metal avg `-0.2654` n `20`; unknown avg `-0.3829` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
