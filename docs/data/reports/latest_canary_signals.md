# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T02:52:28.257050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.0875` n `229`; crypto_major avg `0.1678` n `8`; equity avg `0.0978` n `91`; fx avg `-0.0126` n `6`; index avg `0.0371` n `25`; metal avg `0.0642` n `20`; unknown avg `-0.1024` n `765`
- 1h: commodity avg `0.0231` n `12`; crypto_alt avg `-0.1439` n `229`; crypto_major avg `-0.0139` n `8`; equity avg `0.0305` n `91`; fx avg `-0.0462` n `6`; index avg `0.0041` n `25`; metal avg `0.1472` n `20`; unknown avg `0.052` n `763`
- 4h: commodity avg `0.1056` n `12`; crypto_alt avg `0.7852` n `229`; crypto_major avg `1.0925` n `8`; equity avg `0.1861` n `91`; fx avg `-0.0115` n `6`; index avg `-0.0161` n `25`; metal avg `0.2083` n `20`; unknown avg `0.2134` n `763`
- 24h: commodity avg `-1.064` n `12`; crypto_alt avg `2.0268` n `229`; crypto_major avg `2.2312` n `8`; equity avg `1.9886` n `91`; fx avg `0.012` n `6`; index avg `0.5178` n `25`; metal avg `0.94` n `20`; unknown avg `0.0375` n `746`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
