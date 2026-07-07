# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T04:07:25.782935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.0219` n `229`; crypto_major avg `-0.023` n `8`; equity avg `0.0865` n `91`; fx avg `-0.0001` n `6`; index avg `0.045` n `25`; metal avg `0.0875` n `20`; unknown avg `2.7753` n `763`
- 1h: commodity avg `-0.0475` n `12`; crypto_alt avg `-0.4258` n `229`; crypto_major avg `-0.4582` n `8`; equity avg `-0.4809` n `91`; fx avg `-0.0193` n `6`; index avg `-0.1049` n `25`; metal avg `-0.0922` n `20`; unknown avg `-0.0637` n `763`
- 4h: commodity avg `-0.0556` n `12`; crypto_alt avg `-1.2711` n `229`; crypto_major avg `-1.2331` n `8`; equity avg `-1.2769` n `91`; fx avg `-0.1058` n `6`; index avg `-0.3257` n `25`; metal avg `-0.2633` n `20`; unknown avg `0.9596` n `761`
- 24h: commodity avg `0.2589` n `12`; crypto_alt avg `-0.3732` n `229`; crypto_major avg `-0.949` n `8`; equity avg `-1.3342` n `90`; fx avg `-0.0311` n `6`; index avg `-0.2119` n `25`; metal avg `-0.2361` n `20`; unknown avg `-0.5672` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
