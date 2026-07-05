# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T22:07:26.137770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `0.0308` n `229`; crypto_major avg `0.2447` n `8`; equity avg `-0.0124` n `88`; fx avg `0.0397` n `6`; index avg `-0.0231` n `25`; metal avg `0.0666` n `20`; unknown avg `0.1189` n `765`
- 1h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.672` n `229`; crypto_major avg `0.7306` n `8`; equity avg `0.0155` n `88`; fx avg `0.0602` n `6`; index avg `-0.0325` n `25`; metal avg `0.0392` n `20`; unknown avg `0.9963` n `765`
- 4h: commodity avg `-0.0592` n `12`; crypto_alt avg `0.6107` n `229`; crypto_major avg `0.8427` n `8`; equity avg `0.082` n `88`; fx avg `0.0771` n `6`; index avg `-0.0226` n `25`; metal avg `0.0575` n `20`; unknown avg `1.3939` n `765`
- 24h: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.452` n `229`; crypto_major avg `0.2243` n `8`; equity avg `0.3057` n `88`; fx avg `0.0283` n `6`; index avg `0.0472` n `25`; metal avg `0.0656` n `20`; unknown avg `1.6378` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
