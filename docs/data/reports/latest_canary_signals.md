# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T13:22:25.563375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `-0.1075` n `229`; crypto_major avg `-0.135` n `8`; equity avg `-0.0045` n `88`; fx avg `0.0006` n `6`; index avg `-0.0003` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.0365` n `765`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `0.3987` n `229`; crypto_major avg `0.3106` n `8`; equity avg `0.0114` n `88`; fx avg `-0.0389` n `6`; index avg `-0.003` n `25`; metal avg `0.0171` n `20`; unknown avg `-0.0166` n `765`
- 4h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.0326` n `229`; crypto_major avg `0.4173` n `8`; equity avg `0.0874` n `88`; fx avg `-0.0389` n `6`; index avg `0.0033` n `25`; metal avg `0.0297` n `20`; unknown avg `-0.0016` n `765`
- 24h: commodity avg `-0.0175` n `12`; crypto_alt avg `-1.0939` n `229`; crypto_major avg `-0.5896` n `8`; equity avg `0.2919` n `88`; fx avg `-0.0244` n `6`; index avg `0.0561` n `25`; metal avg `0.0938` n `20`; unknown avg `-1.2916` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
