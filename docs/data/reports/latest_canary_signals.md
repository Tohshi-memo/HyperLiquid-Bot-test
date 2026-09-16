# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T17:07:41.147880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.0023` n `234`; crypto_major avg `-0.0775` n `8`; equity avg `-0.0574` n `137`; fx avg `-0.0042` n `6`; index avg `-0.0198` n `27`; metal avg `-0.0267` n `20`; unknown avg `0.1695` n `915`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `0.24` n `234`; crypto_major avg `0.09` n `8`; equity avg `-0.0767` n `137`; fx avg `-0.0106` n `6`; index avg `-0.0307` n `27`; metal avg `-0.0631` n `20`; unknown avg `1.0661` n `909`
- 4h: commodity avg `-0.4266` n `12`; crypto_alt avg `-0.4678` n `234`; crypto_major avg `-0.0334` n `8`; equity avg `0.3196` n `137`; fx avg `-0.037` n `6`; index avg `0.031` n `27`; metal avg `-0.0361` n `20`; unknown avg `16.4478` n `897`
- 24h: commodity avg `-0.6378` n `12`; crypto_alt avg `-2.5048` n `234`; crypto_major avg `-1.4751` n `8`; equity avg `1.0106` n `137`; fx avg `0.0093` n `6`; index avg `0.2306` n `27`; metal avg `0.3011` n `20`; unknown avg `12.1012` n `814`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
