# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T23:12:43.390791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `-0.1929` n `231`; crypto_major avg `-0.0312` n `8`; equity avg `0.0391` n `122`; fx avg `0.0027` n `6`; index avg `-0.001` n `25`; metal avg `0.0375` n `20`; unknown avg `0.2949` n `794`
- 1h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.3547` n `231`; crypto_major avg `-0.1454` n `8`; equity avg `-0.0306` n `122`; fx avg `0.0046` n `6`; index avg `-0.0018` n `25`; metal avg `0.0795` n `20`; unknown avg `0.3325` n `794`
- 4h: commodity avg `-0.0935` n `12`; crypto_alt avg `0.282` n `231`; crypto_major avg `0.5786` n `8`; equity avg `-0.2525` n `122`; fx avg `-0.008` n `6`; index avg `-0.0405` n `25`; metal avg `0.194` n `20`; unknown avg `-0.4883` n `794`
- 24h: commodity avg `-0.1006` n `12`; crypto_alt avg `-1.6966` n `231`; crypto_major avg `-0.813` n `8`; equity avg `-2.7891` n `122`; fx avg `-0.0576` n `6`; index avg `-0.3397` n `25`; metal avg `0.2962` n `20`; unknown avg `0.8922` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
