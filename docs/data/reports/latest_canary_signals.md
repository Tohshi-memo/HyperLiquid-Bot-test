# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T18:07:33.988912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `13`; crypto_alt avg `0.1409` n `238`; crypto_major avg `0.2394` n `8`; equity avg `-0.0289` n `156`; fx avg `-0.0012` n `6`; index avg `0.0012` n `27`; metal avg `0.0139` n `20`; unknown avg `1.6012` n `1232`
- 1h: commodity avg `0.0008` n `13`; crypto_alt avg `-0.8065` n `238`; crypto_major avg `-0.5689` n `8`; equity avg `-0.4681` n `156`; fx avg `-0.0014` n `6`; index avg `-0.0562` n `27`; metal avg `-0.1173` n `20`; unknown avg `4.321` n `1232`
- 4h: commodity avg `0.1744` n `13`; crypto_alt avg `0.4721` n `238`; crypto_major avg `0.7085` n `8`; equity avg `-0.5733` n `156`; fx avg `0.1127` n `6`; index avg `-0.054` n `27`; metal avg `-0.0177` n `20`; unknown avg `24.2251` n `1174`
- 24h: commodity avg `-0.5483` n `13`; crypto_alt avg `0.3018` n `238`; crypto_major avg `1.8473` n `8`; equity avg `-1.0292` n `155`; fx avg `0.0257` n `6`; index avg `-0.1509` n `27`; metal avg `-0.491` n `20`; unknown avg `35.2683` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
