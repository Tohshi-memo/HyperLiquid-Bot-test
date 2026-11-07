# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T16:37:27.941400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `13`; crypto_alt avg `0.0258` n `239`; crypto_major avg `-0.0136` n `8`; equity avg `-0.0026` n `158`; fx avg `-0.0095` n `6`; index avg `-0.0061` n `27`; metal avg `-0.0116` n `20`; unknown avg `-0.3986` n `1261`
- 1h: commodity avg `0.0391` n `13`; crypto_alt avg `0.0565` n `239`; crypto_major avg `0.0055` n `8`; equity avg `0.0217` n `158`; fx avg `-0.0126` n `6`; index avg `-0.0074` n `27`; metal avg `-0.0156` n `20`; unknown avg `-0.2351` n `1247`
- 4h: commodity avg `0.0362` n `13`; crypto_alt avg `-0.2102` n `239`; crypto_major avg `-0.2235` n `8`; equity avg `-0.0966` n `158`; fx avg `-0.0469` n `6`; index avg `0.0249` n `27`; metal avg `-0.0271` n `20`; unknown avg `-0.4802` n `1241`
- 24h: commodity avg `0.1789` n `13`; crypto_alt avg `-1.6584` n `239`; crypto_major avg `-0.7944` n `8`; equity avg `-0.0841` n `158`; fx avg `-0.0283` n `6`; index avg `-0.052` n `27`; metal avg `0.0092` n `20`; unknown avg `-0.8006` n `1109`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
