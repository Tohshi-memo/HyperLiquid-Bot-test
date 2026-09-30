# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T04:22:31.842016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0613` n `12`; crypto_alt avg `0.3479` n `234`; crypto_major avg `0.1005` n `8`; equity avg `0.0203` n `142`; fx avg `0.0147` n `6`; index avg `0.0081` n `26`; metal avg `0.0236` n `20`; unknown avg `1.3174` n `963`
- 1h: commodity avg `-0.0593` n `12`; crypto_alt avg `0.4567` n `234`; crypto_major avg `0.1961` n `8`; equity avg `0.1069` n `142`; fx avg `0.024` n `6`; index avg `0.0433` n `26`; metal avg `-0.0347` n `20`; unknown avg `3.6668` n `955`
- 4h: commodity avg `0.0311` n `12`; crypto_alt avg `1.0622` n `234`; crypto_major avg `0.4336` n `8`; equity avg `-0.1951` n `142`; fx avg `-0.0214` n `6`; index avg `-0.0309` n `26`; metal avg `-0.0985` n `20`; unknown avg `5.4192` n `955`
- 24h: commodity avg `-0.9966` n `12`; crypto_alt avg `1.5585` n `234`; crypto_major avg `0.1596` n `8`; equity avg `1.0944` n `142`; fx avg `-0.1309` n `6`; index avg `0.192` n `26`; metal avg `0.2423` n `20`; unknown avg `3239.9072` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
