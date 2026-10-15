# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T12:52:36.904190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `13`; crypto_alt avg `0.0091` n `236`; crypto_major avg `0.0117` n `8`; equity avg `0.0358` n `151`; fx avg `-0.007` n `6`; index avg `0.0331` n `26`; metal avg `-0.0418` n `20`; unknown avg `0.491` n `1136`
- 1h: commodity avg `-0.1937` n `13`; crypto_alt avg `-0.5381` n `236`; crypto_major avg `-0.3623` n `8`; equity avg `-0.3641` n `151`; fx avg `-0.003` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0111` n `20`; unknown avg `1.1382` n `1128`
- 4h: commodity avg `-0.1852` n `13`; crypto_alt avg `-0.8479` n `236`; crypto_major avg `-0.7603` n `8`; equity avg `-0.5387` n `151`; fx avg `-0.0124` n `6`; index avg `-0.0152` n `26`; metal avg `0.0521` n `20`; unknown avg `0.1608` n `1048`
- 24h: commodity avg `-0.3577` n `13`; crypto_alt avg `-4.1286` n `236`; crypto_major avg `-3.1793` n `8`; equity avg `-5.2574` n `151`; fx avg `0.142` n `6`; index avg `-0.7717` n `26`; metal avg `-0.1905` n `20`; unknown avg `0.9929` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1208`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0861`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0749`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0653`, n `666`, weak_sample_signal
