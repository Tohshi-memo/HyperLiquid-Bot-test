# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T11:37:28.999081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0522` n `12`; crypto_alt avg `0.1573` n `228`; crypto_major avg `0.1536` n `8`; equity avg `0.1431` n `88`; fx avg `-0.0045` n `6`; index avg `0.0052` n `23`; metal avg `0.0243` n `20`; unknown avg `-0.0087` n `764`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `-0.1782` n `228`; crypto_major avg `-0.3839` n `8`; equity avg `-0.0135` n `88`; fx avg `-0.0039` n `6`; index avg `-0.0085` n `23`; metal avg `-0.0039` n `20`; unknown avg `-0.0023` n `764`
- 4h: commodity avg `0.0583` n `12`; crypto_alt avg `-0.2198` n `228`; crypto_major avg `-0.0573` n `8`; equity avg `0.2742` n `88`; fx avg `0.0192` n `6`; index avg `0.0173` n `23`; metal avg `-0.3138` n `20`; unknown avg `-0.0179` n `764`
- 24h: commodity avg `-0.4469` n `12`; crypto_alt avg `0.1297` n `228`; crypto_major avg `-0.1671` n `8`; equity avg `0.5464` n `88`; fx avg `0.0612` n `6`; index avg `0.0818` n `23`; metal avg `-0.5166` n `20`; unknown avg `0.833` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
