# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T01:07:24.995033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.359` n `229`; crypto_major avg `-0.3232` n `8`; equity avg `-0.12` n `91`; fx avg `-0.0028` n `6`; index avg `-0.053` n `25`; metal avg `-0.1437` n `20`; unknown avg `0.3982` n `763`
- 1h: commodity avg `-0.026` n `12`; crypto_alt avg `-0.2538` n `229`; crypto_major avg `0.0371` n `8`; equity avg `-0.4207` n `91`; fx avg `-0.011` n `6`; index avg `-0.1351` n `25`; metal avg `-0.2404` n `20`; unknown avg `0.4932` n `763`
- 4h: commodity avg `0.0489` n `12`; crypto_alt avg `-0.2085` n `229`; crypto_major avg `-0.0718` n `8`; equity avg `-0.9027` n `91`; fx avg `0.0072` n `6`; index avg `-0.2739` n `25`; metal avg `-0.3035` n `20`; unknown avg `1.7784` n `763`
- 24h: commodity avg `0.3076` n `12`; crypto_alt avg `0.0624` n `229`; crypto_major avg `-0.6778` n `8`; equity avg `-1.2566` n `90`; fx avg `0.114` n `6`; index avg `-0.2438` n `25`; metal avg `-0.5222` n `20`; unknown avg `-0.3393` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
