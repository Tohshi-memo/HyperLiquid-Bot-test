# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T23:07:26.242641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.0236` n `229`; crypto_major avg `-0.0742` n `8`; equity avg `-0.0068` n `88`; fx avg `0.0206` n `6`; index avg `0.0054` n `25`; metal avg `0.0079` n `20`; unknown avg `0.1042` n `765`
- 1h: commodity avg `-0.0314` n `12`; crypto_alt avg `-0.176` n `229`; crypto_major avg `-0.195` n `8`; equity avg `-0.0894` n `88`; fx avg `-0.002` n `6`; index avg `0.0019` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.196` n `765`
- 4h: commodity avg `-0.017` n `12`; crypto_alt avg `0.5325` n `229`; crypto_major avg `0.4711` n `8`; equity avg `-0.0297` n `88`; fx avg `-0.0188` n `6`; index avg `-0.0371` n `25`; metal avg `0.0094` n `20`; unknown avg `-0.4987` n `765`
- 24h: commodity avg `0.1477` n `12`; crypto_alt avg `3.1973` n `229`; crypto_major avg `3.4327` n `8`; equity avg `1.8847` n `88`; fx avg `-0.0659` n `6`; index avg `0.4736` n `25`; metal avg `0.5304` n `20`; unknown avg `5.162` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
