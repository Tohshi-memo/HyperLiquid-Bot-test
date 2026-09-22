# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T23:37:32.456591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `-0.5543` n `234`; crypto_major avg `-0.5083` n `8`; equity avg `0.0195` n `140`; fx avg `-0.0309` n `6`; index avg `0.0022` n `26`; metal avg `-0.0058` n `20`; unknown avg `1.0914` n `945`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.5166` n `234`; crypto_major avg `-0.0549` n `8`; equity avg `0.0375` n `140`; fx avg `-0.0351` n `6`; index avg `0.0013` n `26`; metal avg `0.0282` n `20`; unknown avg `1.1015` n `943`
- 4h: commodity avg `0.1737` n `12`; crypto_alt avg `1.3648` n `234`; crypto_major avg `0.0231` n `8`; equity avg `0.1258` n `140`; fx avg `-0.0506` n `6`; index avg `-0.0271` n `26`; metal avg `-0.0571` n `20`; unknown avg `2.0665` n `906`
- 24h: commodity avg `0.1224` n `12`; crypto_alt avg `3.021` n `234`; crypto_major avg `0.4529` n `8`; equity avg `0.7546` n `140`; fx avg `-0.3055` n `6`; index avg `0.0986` n `26`; metal avg `0.2145` n `20`; unknown avg `1.0442` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
