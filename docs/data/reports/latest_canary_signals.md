# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T13:52:29.839086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0362` n `12`; crypto_alt avg `-0.0873` n `228`; crypto_major avg `-0.2819` n `8`; equity avg `-0.0261` n `88`; fx avg `0.0052` n `6`; index avg `0.0346` n `23`; metal avg `-0.025` n `20`; unknown avg `0.1653` n `764`
- 1h: commodity avg `0.0614` n `12`; crypto_alt avg `-0.1861` n `228`; crypto_major avg `-0.0632` n `8`; equity avg `-0.118` n `88`; fx avg `0.0013` n `6`; index avg `-0.001` n `23`; metal avg `-0.1391` n `20`; unknown avg `0.5919` n `764`
- 4h: commodity avg `-0.1938` n `12`; crypto_alt avg `-0.1716` n `228`; crypto_major avg `0.1922` n `8`; equity avg `-0.0534` n `88`; fx avg `0.044` n `6`; index avg `-0.0138` n `23`; metal avg `0.058` n `20`; unknown avg `1.1928` n `764`
- 24h: commodity avg `-0.5641` n `12`; crypto_alt avg `0.1277` n `228`; crypto_major avg `0.0198` n `8`; equity avg `0.2788` n `88`; fx avg `0.1096` n `6`; index avg `0.0366` n `23`; metal avg `-0.491` n `20`; unknown avg `1.7042` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
