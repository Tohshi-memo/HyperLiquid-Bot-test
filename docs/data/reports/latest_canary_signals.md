# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T07:37:28.428388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `13`; crypto_alt avg `-0.1936` n `239`; crypto_major avg `-0.0991` n `8`; equity avg `-0.3165` n `158`; fx avg `-0.0424` n `6`; index avg `-0.0529` n `27`; metal avg `-0.0626` n `20`; unknown avg `0.0287` n `1256`
- 1h: commodity avg `-0.0373` n `13`; crypto_alt avg `-0.6091` n `239`; crypto_major avg `-0.6675` n `8`; equity avg `-0.5003` n `158`; fx avg `-0.0982` n `6`; index avg `-0.0812` n `27`; metal avg `-0.0985` n `20`; unknown avg `-0.422` n `1248`
- 4h: commodity avg `-0.0584` n `13`; crypto_alt avg `-0.1019` n `239`; crypto_major avg `-0.5949` n `8`; equity avg `-0.6253` n `158`; fx avg `-0.1527` n `6`; index avg `-0.1373` n `27`; metal avg `-0.0906` n `20`; unknown avg `-0.6099` n `1218`
- 24h: commodity avg `1.2124` n `13`; crypto_alt avg `-4.2733` n `239`; crypto_major avg `-6.1147` n `8`; equity avg `-6.4508` n `158`; fx avg `-0.0554` n `6`; index avg `-0.8844` n `27`; metal avg `-0.4972` n `20`; unknown avg `233.8239` n `1031`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
