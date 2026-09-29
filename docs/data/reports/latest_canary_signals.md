# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T01:07:25.188682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `-0.3678` n `234`; crypto_major avg `-0.2343` n `8`; equity avg `-0.0542` n `141`; fx avg `-0.0399` n `6`; index avg `0.0082` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.0442` n `961`
- 1h: commodity avg `0.0001` n `12`; crypto_alt avg `-0.9245` n `234`; crypto_major avg `-0.6433` n `8`; equity avg `-0.4017` n `141`; fx avg `-0.0229` n `6`; index avg `-0.0711` n `26`; metal avg `-0.0636` n `20`; unknown avg `0.4279` n `961`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `-0.3476` n `234`; crypto_major avg `-0.6448` n `8`; equity avg `-0.2772` n `141`; fx avg `-0.0462` n `6`; index avg `-0.0518` n `26`; metal avg `-0.0201` n `20`; unknown avg `-0.0768` n `931`
- 24h: commodity avg `0.1687` n `12`; crypto_alt avg `-4.0672` n `234`; crypto_major avg `-2.2548` n `8`; equity avg `-2.8634` n `141`; fx avg `-0.0514` n `6`; index avg `-0.2661` n `26`; metal avg `-0.7089` n `20`; unknown avg `160.8507` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
