# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T10:07:26.764458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0213` n `13`; crypto_alt avg `0.0285` n `239`; crypto_major avg `-0.0279` n `8`; equity avg `0.008` n `162`; fx avg `-0.0324` n `6`; index avg `-0.0001` n `27`; metal avg `-0.0721` n `20`; unknown avg `-0.0597` n `1260`
- 1h: commodity avg `0.0584` n `13`; crypto_alt avg `-0.1274` n `239`; crypto_major avg `-0.0672` n `8`; equity avg `-0.1643` n `162`; fx avg `-0.0082` n `6`; index avg `-0.0029` n `27`; metal avg `-0.0882` n `20`; unknown avg `-0.0279` n `1262`
- 4h: commodity avg `0.2625` n `13`; crypto_alt avg `-0.5786` n `239`; crypto_major avg `-0.7211` n `8`; equity avg `-0.7384` n `162`; fx avg `-0.0752` n `6`; index avg `-0.0422` n `27`; metal avg `-0.2` n `20`; unknown avg `210.1998` n `1188`
- 24h: commodity avg `-0.8212` n `13`; crypto_alt avg `0.5684` n `239`; crypto_major avg `0.9198` n `8`; equity avg `-2.8991` n `162`; fx avg `-0.0605` n `6`; index avg `-0.2999` n `27`; metal avg `-0.1373` n `20`; unknown avg `16.6252` n `1113`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
