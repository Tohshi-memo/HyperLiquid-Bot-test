# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T19:07:34.982238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0326` n `12`; crypto_alt avg `0.1822` n `228`; crypto_major avg `0.1703` n `8`; equity avg `0.1453` n `88`; fx avg `-0.0005` n `6`; index avg `0.0134` n `25`; metal avg `0.07` n `20`; unknown avg `-0.0985` n `763`
- 1h: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.374` n `228`; crypto_major avg `-0.0568` n `8`; equity avg `-0.2406` n `88`; fx avg `0.0008` n `6`; index avg `-0.0053` n `25`; metal avg `-0.0346` n `20`; unknown avg `-0.4183` n `761`
- 4h: commodity avg `-0.0232` n `12`; crypto_alt avg `-0.5276` n `228`; crypto_major avg `0.1987` n `8`; equity avg `-0.3325` n `88`; fx avg `-0.0145` n `6`; index avg `-0.084` n `25`; metal avg `-0.1622` n `20`; unknown avg `-0.0634` n `761`
- 24h: commodity avg `-0.5531` n `12`; crypto_alt avg `1.4116` n `228`; crypto_major avg `1.6592` n `8`; equity avg `-0.9345` n `88`; fx avg `-0.0067` n `6`; index avg `-0.4873` n `25`; metal avg `0.1922` n `20`; unknown avg `0.5221` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
