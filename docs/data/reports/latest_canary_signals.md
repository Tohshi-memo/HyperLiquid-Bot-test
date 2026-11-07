# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T23:07:33.764960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.03` n `239`; crypto_major avg `0.009` n `8`; equity avg `0.0307` n `158`; fx avg `-0.0048` n `6`; index avg `0.0007` n `27`; metal avg `0.0001` n `20`; unknown avg `0.3382` n `1242`
- 1h: commodity avg `0.006` n `13`; crypto_alt avg `0.267` n `239`; crypto_major avg `0.1229` n `8`; equity avg `0.0762` n `158`; fx avg `-0.0123` n `6`; index avg `-0.002` n `27`; metal avg `0.004` n `20`; unknown avg `-0.0864` n `1240`
- 4h: commodity avg `0.0731` n `13`; crypto_alt avg `-0.4982` n `239`; crypto_major avg `-0.2409` n `8`; equity avg `-0.1287` n `158`; fx avg `0.0014` n `6`; index avg `-0.0249` n `27`; metal avg `-0.0098` n `20`; unknown avg `1.1847` n `1198`
- 24h: commodity avg `0.0554` n `13`; crypto_alt avg `-1.2742` n `239`; crypto_major avg `-0.6217` n `8`; equity avg `-0.0778` n `158`; fx avg `-0.0279` n `6`; index avg `0.0506` n `27`; metal avg `-0.0321` n `20`; unknown avg `160.3663` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
