# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T09:22:25.846105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0337` n `13`; crypto_alt avg `-0.306` n `239`; crypto_major avg `-0.25` n `8`; equity avg `-0.0055` n `158`; fx avg `0.0043` n `6`; index avg `-0.0121` n `27`; metal avg `-0.0012` n `20`; unknown avg `0.01` n `1262`
- 1h: commodity avg `-0.0576` n `13`; crypto_alt avg `-0.3886` n `239`; crypto_major avg `-0.2197` n `8`; equity avg `0.0017` n `158`; fx avg `0.0012` n `6`; index avg `-0.0515` n `27`; metal avg `0.0048` n `20`; unknown avg `-0.143` n `1256`
- 4h: commodity avg `-0.002` n `13`; crypto_alt avg `-0.3727` n `239`; crypto_major avg `-0.1974` n `8`; equity avg `0.1045` n `158`; fx avg `0.0202` n `6`; index avg `-0.0105` n `27`; metal avg `0.0154` n `20`; unknown avg `-0.0724` n `1204`
- 24h: commodity avg `0.096` n `13`; crypto_alt avg `-1.9803` n `239`; crypto_major avg `-0.9132` n `8`; equity avg `-0.12` n `158`; fx avg `0.0587` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0254` n `20`; unknown avg `1.5392` n `1119`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
