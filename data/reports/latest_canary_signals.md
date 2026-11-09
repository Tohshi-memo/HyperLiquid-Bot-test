# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T05:52:27.816185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `13`; crypto_alt avg `0.1025` n `239`; crypto_major avg `-0.0563` n `8`; equity avg `-0.3132` n `158`; fx avg `0.0004` n `6`; index avg `-0.0505` n `27`; metal avg `0.0061` n `20`; unknown avg `0.5615` n `1259`
- 1h: commodity avg `-0.2098` n `13`; crypto_alt avg `-0.3279` n `239`; crypto_major avg `-0.4784` n `8`; equity avg `-0.6989` n `158`; fx avg `-0.0135` n `6`; index avg `-0.1079` n `27`; metal avg `-0.0344` n `20`; unknown avg `48.2151` n `1251`
- 4h: commodity avg `0.1111` n `13`; crypto_alt avg `-0.742` n `239`; crypto_major avg `-1.0759` n `8`; equity avg `-0.6371` n `158`; fx avg `-0.0591` n `6`; index avg `-0.109` n `27`; metal avg `-0.0258` n `20`; unknown avg `3.8248` n `1234`
- 24h: commodity avg `-0.0045` n `13`; crypto_alt avg `-2.1164` n `239`; crypto_major avg `-2.979` n `8`; equity avg `-0.3219` n `158`; fx avg `-0.1122` n `6`; index avg `-0.0429` n `27`; metal avg `0.4787` n `20`; unknown avg `2.1451` n `980`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
