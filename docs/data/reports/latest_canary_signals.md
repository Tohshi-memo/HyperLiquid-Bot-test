# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T10:07:28.804024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `0.1493` n `239`; crypto_major avg `0.3764` n `8`; equity avg `0.2905` n `168`; fx avg `0.0117` n `6`; index avg `0.0268` n `27`; metal avg `0.1071` n `20`; unknown avg `0.4157` n `1255`
- 1h: commodity avg `0.2213` n `13`; crypto_alt avg `-0.6156` n `239`; crypto_major avg `-0.3606` n `8`; equity avg `-0.5876` n `168`; fx avg `-0.0201` n `6`; index avg `-0.0794` n `27`; metal avg `-0.0158` n `20`; unknown avg `0.5334` n `1257`
- 4h: commodity avg `0.0503` n `13`; crypto_alt avg `-0.4156` n `239`; crypto_major avg `-0.61` n `8`; equity avg `-1.2722` n `168`; fx avg `-0.02` n `6`; index avg `-0.1425` n `27`; metal avg `0.1517` n `20`; unknown avg `0.6321` n `1227`
- 24h: commodity avg `0.4097` n `13`; crypto_alt avg `-2.1204` n `239`; crypto_major avg `-2.8336` n `8`; equity avg `-4.9168` n `167`; fx avg `-0.0073` n `6`; index avg `-0.439` n `27`; metal avg `-0.7861` n `20`; unknown avg `451.8635` n `1047`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
