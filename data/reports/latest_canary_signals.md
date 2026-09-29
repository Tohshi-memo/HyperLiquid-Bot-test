# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T08:22:37.024108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1778` n `12`; crypto_alt avg `0.5892` n `234`; crypto_major avg `0.4145` n `8`; equity avg `0.2831` n `141`; fx avg `0.0032` n `6`; index avg `0.0331` n `26`; metal avg `0.0684` n `20`; unknown avg `0.0394` n `963`
- 1h: commodity avg `-0.2521` n `12`; crypto_alt avg `0.6873` n `234`; crypto_major avg `0.4281` n `8`; equity avg `0.3758` n `141`; fx avg `-0.0041` n `6`; index avg `0.0393` n `26`; metal avg `0.0058` n `20`; unknown avg `0.3975` n `945`
- 4h: commodity avg `-0.3404` n `12`; crypto_alt avg `2.0735` n `234`; crypto_major avg `1.4118` n `8`; equity avg `1.0232` n `141`; fx avg `-0.0243` n `6`; index avg `0.1453` n `26`; metal avg `0.0863` n `20`; unknown avg `1.7062` n `927`
- 24h: commodity avg `-0.3841` n `12`; crypto_alt avg `1.4359` n `234`; crypto_major avg `1.4439` n `8`; equity avg `-0.0647` n `141`; fx avg `-0.0131` n `6`; index avg `-0.0147` n `26`; metal avg `-0.1921` n `20`; unknown avg `48.7149` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
