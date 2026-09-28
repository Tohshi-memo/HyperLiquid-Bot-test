# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T19:52:28.477775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `12`; crypto_alt avg `0.0694` n `234`; crypto_major avg `0.1846` n `8`; equity avg `-0.0933` n `141`; fx avg `0.0032` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0482` n `20`; unknown avg `112.2501` n `963`
- 1h: commodity avg `0.129` n `12`; crypto_alt avg `-1.2224` n `234`; crypto_major avg `-0.9868` n `8`; equity avg `-0.3861` n `141`; fx avg `0.0044` n `6`; index avg `-0.0488` n `26`; metal avg `-0.0999` n `20`; unknown avg `23.6311` n `921`
- 4h: commodity avg `-0.3643` n `12`; crypto_alt avg `0.1336` n `234`; crypto_major avg `0.0619` n `8`; equity avg `0.3871` n `141`; fx avg `-0.0009` n `6`; index avg `0.087` n `26`; metal avg `0.0468` n `20`; unknown avg `36.4597` n `914`
- 24h: commodity avg `-0.3603` n `12`; crypto_alt avg `-4.2075` n `234`; crypto_major avg `-2.3347` n `8`; equity avg `-3.3334` n `141`; fx avg `0.0402` n `6`; index avg `-0.3148` n `26`; metal avg `-1.0733` n `20`; unknown avg `31.7527` n `806`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
