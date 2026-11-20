# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T06:22:27.672276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1428` n `13`; crypto_alt avg `-0.0201` n `239`; crypto_major avg `0.0487` n `8`; equity avg `0.0463` n `165`; fx avg `0.0202` n `6`; index avg `0.0188` n `27`; metal avg `0.0607` n `20`; unknown avg `7.3984` n `1260`
- 1h: commodity avg `0.027` n `13`; crypto_alt avg `0.8071` n `239`; crypto_major avg `0.7905` n `8`; equity avg `0.3655` n `165`; fx avg `0.0421` n `6`; index avg `0.0351` n `27`; metal avg `0.44` n `20`; unknown avg `61.5576` n `1240`
- 4h: commodity avg `0.0303` n `13`; crypto_alt avg `0.2962` n `239`; crypto_major avg `0.6506` n `8`; equity avg `-0.4003` n `165`; fx avg `0.0456` n `6`; index avg `-0.0702` n `27`; metal avg `0.2656` n `20`; unknown avg `487.9964` n `1228`
- 24h: commodity avg `-0.0699` n `13`; crypto_alt avg `-2.9469` n `239`; crypto_major avg `-2.4168` n `8`; equity avg `-6.3165` n `165`; fx avg `0.0634` n `6`; index avg `-0.5585` n `27`; metal avg `-1.4986` n `20`; unknown avg `296.8535` n `1169`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
