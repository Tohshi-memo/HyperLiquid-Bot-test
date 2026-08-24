# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T16:51:57.651050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0348` n `12`; crypto_alt avg `-0.1666` n `231`; crypto_major avg `-0.3874` n `8`; equity avg `-0.187` n `122`; fx avg `0.0144` n `6`; index avg `-0.0217` n `25`; metal avg `-0.0433` n `20`; unknown avg `0.0225` n `793`
- 1h: commodity avg `0.0944` n `12`; crypto_alt avg `0.188` n `231`; crypto_major avg `0.0198` n `8`; equity avg `-0.0873` n `122`; fx avg `-0.0101` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0185` n `20`; unknown avg `-0.0022` n `793`
- 4h: commodity avg `-0.1938` n `12`; crypto_alt avg `-0.3898` n `231`; crypto_major avg `-0.696` n `8`; equity avg `-0.6907` n `122`; fx avg `0.0091` n `6`; index avg `-0.1043` n `25`; metal avg `-0.0524` n `20`; unknown avg `0.3902` n `793`
- 24h: commodity avg `-0.17` n `12`; crypto_alt avg `-0.3842` n `231`; crypto_major avg `0.2496` n `8`; equity avg `-2.3195` n `122`; fx avg `-0.1369` n `6`; index avg `-0.2873` n `25`; metal avg `0.1457` n `20`; unknown avg `3.9762` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
