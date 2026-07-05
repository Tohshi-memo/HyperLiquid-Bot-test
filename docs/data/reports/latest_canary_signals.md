# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T20:43:06.958553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.0987` n `229`; crypto_major avg `-0.1138` n `8`; equity avg `0.0054` n `88`; fx avg `-0.0136` n `6`; index avg `-0.0017` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.0344` n `765`
- 1h: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.1203` n `229`; crypto_major avg `-0.0564` n `8`; equity avg `0.0411` n `88`; fx avg `-0.0237` n `6`; index avg `-0.0036` n `25`; metal avg `0.0047` n `20`; unknown avg `0.0584` n `765`
- 4h: commodity avg `-0.0607` n `12`; crypto_alt avg `0.3603` n `229`; crypto_major avg `0.2712` n `8`; equity avg `0.1451` n `88`; fx avg `-0.0148` n `6`; index avg `0.0047` n `25`; metal avg `0.0115` n `20`; unknown avg `0.7473` n `765`
- 24h: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.9019` n `229`; crypto_major avg `-0.3713` n `8`; equity avg `0.3684` n `88`; fx avg `-0.0467` n `6`; index avg `0.0842` n `25`; metal avg `0.0557` n `20`; unknown avg `1.1199` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
