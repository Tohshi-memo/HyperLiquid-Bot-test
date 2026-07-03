# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T20:37:30.177688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.49` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0166` n `12`; crypto_alt avg `0.2463` n `229`; crypto_major avg `0.2844` n `8`; equity avg `0.0776` n `88`; fx avg `-0.0152` n `6`; index avg `-0.012` n `25`; metal avg `0.0212` n `20`; unknown avg `0.3331` n `765`
- 1h: commodity avg `-0.0373` n `12`; crypto_alt avg `0.5295` n `229`; crypto_major avg `0.5928` n `8`; equity avg `-0.0696` n `88`; fx avg `-0.0216` n `6`; index avg `-0.0268` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.5298` n `765`
- 4h: commodity avg `-0.0308` n `12`; crypto_alt avg `1.0069` n `229`; crypto_major avg `1.3841` n `8`; equity avg `0.0401` n `88`; fx avg `-0.0295` n `6`; index avg `-0.0338` n `25`; metal avg `0.0265` n `20`; unknown avg `1.7593` n `765`
- 24h: commodity avg `0.1302` n `12`; crypto_alt avg `3.5642` n `229`; crypto_major avg `3.6275` n `8`; equity avg `1.791` n `88`; fx avg `-0.0906` n `6`; index avg `0.4794` n `25`; metal avg `0.5493` n `20`; unknown avg `8.1885` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
