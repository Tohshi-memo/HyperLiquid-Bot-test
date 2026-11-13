# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T02:37:24.906347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0571` n `13`; crypto_alt avg `-0.4037` n `239`; crypto_major avg `-0.4185` n `8`; equity avg `-0.0437` n `162`; fx avg `-0.0042` n `6`; index avg `0.0132` n `27`; metal avg `0.0405` n `20`; unknown avg `4.9851` n `1262`
- 1h: commodity avg `0.1026` n `13`; crypto_alt avg `-0.6777` n `239`; crypto_major avg `-0.7844` n `8`; equity avg `-0.3626` n `162`; fx avg `0.0301` n `6`; index avg `-0.025` n `27`; metal avg `0.0172` n `20`; unknown avg `4.2569` n `1260`
- 4h: commodity avg `-0.057` n `13`; crypto_alt avg `-0.407` n `239`; crypto_major avg `-0.5592` n `8`; equity avg `0.4734` n `162`; fx avg `0.0026` n `6`; index avg `0.1168` n `27`; metal avg `0.3128` n `20`; unknown avg `164.7929` n `1221`
- 24h: commodity avg `0.8297` n `13`; crypto_alt avg `-1.4656` n `239`; crypto_major avg `-2.635` n `8`; equity avg `-1.0672` n `162`; fx avg `-0.0779` n `6`; index avg `0.047` n `27`; metal avg `-0.373` n `20`; unknown avg `51.2707` n `1121`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
