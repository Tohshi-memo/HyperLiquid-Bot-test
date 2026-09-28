# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T23:07:31.637442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.279` n `234`; crypto_major avg `0.088` n `8`; equity avg `0.0216` n `141`; fx avg `0.0` n `6`; index avg `-0.0018` n `26`; metal avg `0.0069` n `20`; unknown avg `-0.0261` n `961`
- 1h: commodity avg `-0.013` n `12`; crypto_alt avg `1.0828` n `234`; crypto_major avg `0.7326` n `8`; equity avg `0.0937` n `141`; fx avg `-0.0015` n `6`; index avg `0.0019` n `26`; metal avg `-0.0173` n `20`; unknown avg `1.2043` n `961`
- 4h: commodity avg `0.1624` n `12`; crypto_alt avg `-0.1175` n `234`; crypto_major avg `-0.4082` n `8`; equity avg `-0.1745` n `141`; fx avg `0.0029` n `6`; index avg `-0.0111` n `26`; metal avg `-0.0887` n `20`; unknown avg `-0.3374` n `835`
- 24h: commodity avg `0.0696` n `12`; crypto_alt avg `-3.1555` n `234`; crypto_major avg `-1.5183` n `8`; equity avg `-2.9146` n `141`; fx avg `0.0663` n `6`; index avg `-0.2036` n `26`; metal avg `-0.9431` n `20`; unknown avg `90.8112` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
