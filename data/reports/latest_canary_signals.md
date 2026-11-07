# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T07:37:25.238370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `13`; crypto_alt avg `-0.0826` n `239`; crypto_major avg `-0.0645` n `8`; equity avg `-0.0054` n `158`; fx avg `-0.0044` n `6`; index avg `-0.0118` n `27`; metal avg `-0.0011` n `20`; unknown avg `0.0044` n `1261`
- 1h: commodity avg `0.0614` n `13`; crypto_alt avg `0.068` n `239`; crypto_major avg `-0.0197` n `8`; equity avg `-0.0028` n `158`; fx avg `-0.0098` n `6`; index avg `-0.0016` n `27`; metal avg `0.0017` n `20`; unknown avg `11.5349` n `1251`
- 4h: commodity avg `0.0267` n `13`; crypto_alt avg `0.3255` n `239`; crypto_major avg `0.1965` n `8`; equity avg `-0.1041` n `158`; fx avg `-0.0124` n `6`; index avg `0.0006` n `27`; metal avg `-0.0083` n `20`; unknown avg `12.1381` n `1207`
- 24h: commodity avg `-0.2783` n `13`; crypto_alt avg `0.764` n `239`; crypto_major avg `0.7785` n `8`; equity avg `1.7085` n `158`; fx avg `0.0473` n `6`; index avg `0.2837` n `27`; metal avg `0.3146` n `20`; unknown avg `8.8216` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
