# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T07:02:47.840551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `13`; crypto_alt avg `-0.2727` n `239`; crypto_major avg `-0.2651` n `8`; equity avg `-0.0144` n `158`; fx avg `-0.0071` n `6`; index avg `-0.0034` n `27`; metal avg `-0.0226` n `20`; unknown avg `-0.0803` n `1252`
- 1h: commodity avg `-0.0149` n `13`; crypto_alt avg `0.2307` n `239`; crypto_major avg `-0.0917` n `8`; equity avg `0.2634` n `158`; fx avg `-0.0571` n `6`; index avg `0.0174` n `27`; metal avg `0.0046` n `20`; unknown avg `204.6748` n `1242`
- 4h: commodity avg `0.0632` n `13`; crypto_alt avg `-0.3865` n `239`; crypto_major avg `-1.0558` n `8`; equity avg `-0.6712` n `158`; fx avg `-0.1093` n `6`; index avg `-0.1085` n `27`; metal avg `-0.1421` n `20`; unknown avg `-0.6042` n `1218`
- 24h: commodity avg `1.4234` n `13`; crypto_alt avg `-4.4891` n `239`; crypto_major avg `-6.2806` n `8`; equity avg `-6.2753` n `158`; fx avg `-0.0164` n `6`; index avg `-0.8192` n `27`; metal avg `-0.5243` n `20`; unknown avg `233.257` n `1029`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
