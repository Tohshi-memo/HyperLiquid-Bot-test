# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T19:52:28.138345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `13`; crypto_alt avg `0.0521` n `239`; crypto_major avg `0.0041` n `8`; equity avg `0.1339` n `158`; fx avg `-0.0097` n `6`; index avg `0.0028` n `27`; metal avg `-0.0116` n `20`; unknown avg `-0.0586` n `1261`
- 1h: commodity avg `0.18` n `13`; crypto_alt avg `-0.1436` n `239`; crypto_major avg `-0.1336` n `8`; equity avg `0.0292` n `158`; fx avg `-0.0045` n `6`; index avg `-0.0179` n `27`; metal avg `-0.1178` n `20`; unknown avg `1.44` n `1255`
- 4h: commodity avg `0.4601` n `13`; crypto_alt avg `-0.3769` n `239`; crypto_major avg `-0.237` n `8`; equity avg `-0.1488` n `158`; fx avg `-0.0091` n `6`; index avg `-0.0758` n `27`; metal avg `-0.0245` n `20`; unknown avg `66.3375` n `1247`
- 24h: commodity avg `0.217` n `13`; crypto_alt avg `0.4936` n `239`; crypto_major avg `-0.9173` n `8`; equity avg `0.596` n `158`; fx avg `-0.1094` n `6`; index avg `0.0696` n `27`; metal avg `-0.3506` n `20`; unknown avg `54.7458` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
