# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T05:52:29.987329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0356` n `12`; crypto_alt avg `0.3118` n `228`; crypto_major avg `0.3648` n `8`; equity avg `0.2849` n `88`; fx avg `-0.0433` n `6`; index avg `0.0977` n `23`; metal avg `0.2548` n `20`; unknown avg `0.3881` n `764`
- 1h: commodity avg `-0.1094` n `12`; crypto_alt avg `0.1542` n `228`; crypto_major avg `0.2823` n `8`; equity avg `0.4407` n `88`; fx avg `-0.0313` n `6`; index avg `0.208` n `23`; metal avg `0.1055` n `20`; unknown avg `1.3313` n `764`
- 4h: commodity avg `-0.1257` n `12`; crypto_alt avg `0.3459` n `228`; crypto_major avg `0.231` n `8`; equity avg `0.3401` n `88`; fx avg `-0.0025` n `6`; index avg `0.1296` n `23`; metal avg `0.0573` n `20`; unknown avg `-0.5573` n `764`
- 24h: commodity avg `-0.3784` n `12`; crypto_alt avg `0.1386` n `228`; crypto_major avg `0.1975` n `8`; equity avg `0.3433` n `88`; fx avg `0.0179` n `6`; index avg `0.1042` n `23`; metal avg `-0.2208` n `20`; unknown avg `-0.9254` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
