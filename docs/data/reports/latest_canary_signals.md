# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T16:07:27.492574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1632` n `12`; crypto_alt avg `0.1525` n `229`; crypto_major avg `0.1011` n `8`; equity avg `0.1912` n `91`; fx avg `-0.0094` n `6`; index avg `0.0534` n `25`; metal avg `0.0315` n `20`; unknown avg `-0.0001` n `766`
- 1h: commodity avg `-0.0279` n `12`; crypto_alt avg `0.0233` n `229`; crypto_major avg `0.021` n `8`; equity avg `0.2364` n `91`; fx avg `-0.0308` n `6`; index avg `0.0794` n `25`; metal avg `0.0916` n `20`; unknown avg `-0.1538` n `766`
- 4h: commodity avg `-0.483` n `12`; crypto_alt avg `-0.3065` n `229`; crypto_major avg `-0.608` n `8`; equity avg `-0.5283` n `91`; fx avg `-0.0905` n `6`; index avg `0.1089` n `25`; metal avg `0.1346` n `20`; unknown avg `-0.2737` n `766`
- 24h: commodity avg `-0.4937` n `12`; crypto_alt avg `0.8576` n `229`; crypto_major avg `1.0541` n `8`; equity avg `-1.1394` n `91`; fx avg `-0.1649` n `6`; index avg `0.021` n `25`; metal avg `-0.1422` n `20`; unknown avg `-0.2693` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
