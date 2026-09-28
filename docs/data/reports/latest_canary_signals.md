# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T18:07:37.843848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `0.23` n `234`; crypto_major avg `0.0429` n `8`; equity avg `0.051` n `141`; fx avg `-0.005` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0175` n `20`; unknown avg `1.0995` n `961`
- 1h: commodity avg `-0.1885` n `12`; crypto_alt avg `1.0539` n `234`; crypto_major avg `0.584` n `8`; equity avg `0.3664` n `141`; fx avg `-0.004` n `6`; index avg `0.0473` n `26`; metal avg `0.0721` n `20`; unknown avg `3.089` n `960`
- 4h: commodity avg `-0.3362` n `12`; crypto_alt avg `0.3015` n `234`; crypto_major avg `0.3199` n `8`; equity avg `-0.0245` n `141`; fx avg `0.0367` n `6`; index avg `0.0065` n `26`; metal avg `-0.0069` n `20`; unknown avg `18.071` n `928`
- 24h: commodity avg `-0.5503` n `12`; crypto_alt avg `-2.6258` n `234`; crypto_major avg `-1.2522` n `8`; equity avg `-2.9105` n `141`; fx avg `0.045` n `6`; index avg `-0.2627` n `26`; metal avg `-0.9571` n `20`; unknown avg `25.1839` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.181`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
