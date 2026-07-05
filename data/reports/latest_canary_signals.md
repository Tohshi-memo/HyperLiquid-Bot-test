# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T21:22:27.264427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `0.4288` n `229`; crypto_major avg `0.4198` n `8`; equity avg `0.0094` n `88`; fx avg `-0.0061` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.0825` n `765`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `0.2257` n `229`; crypto_major avg `0.2848` n `8`; equity avg `-0.0149` n `88`; fx avg `0.0113` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0077` n `20`; unknown avg `-0.1169` n `765`
- 4h: commodity avg `-0.0368` n `12`; crypto_alt avg `0.5262` n `229`; crypto_major avg `0.5631` n `8`; equity avg `0.1248` n `88`; fx avg `0.0089` n `6`; index avg `0.0065` n `25`; metal avg `0.0113` n `20`; unknown avg `0.726` n `765`
- 24h: commodity avg `0.034` n `12`; crypto_alt avg `-0.9421` n `229`; crypto_major avg `-0.2615` n `8`; equity avg `0.3084` n `88`; fx avg `-0.0368` n `6`; index avg `0.0873` n `25`; metal avg `0.0228` n `20`; unknown avg `1.1005` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
