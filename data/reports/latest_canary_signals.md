# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T08:52:27.294290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `0.1079` n `234`; crypto_major avg `0.1586` n `8`; equity avg `-0.0922` n `141`; fx avg `0.039` n `6`; index avg `-0.0126` n `26`; metal avg `0.0119` n `20`; unknown avg `10.8017` n `962`
- 1h: commodity avg `0.1375` n `12`; crypto_alt avg `0.3353` n `234`; crypto_major avg `0.2504` n `8`; equity avg `-0.4092` n `141`; fx avg `-0.0797` n `6`; index avg `-0.0334` n `26`; metal avg `-0.0195` n `20`; unknown avg `8.9809` n `944`
- 4h: commodity avg `0.1532` n `12`; crypto_alt avg `-1.9087` n `234`; crypto_major avg `-0.9106` n `8`; equity avg `-1.2994` n `141`; fx avg `-0.0405` n `6`; index avg `-0.1121` n `26`; metal avg `-0.2862` n `20`; unknown avg `30.8646` n `920`
- 24h: commodity avg `-0.1414` n `12`; crypto_alt avg `-4.0076` n `234`; crypto_major avg `-3.0712` n `8`; equity avg `-2.8182` n `141`; fx avg `0.0219` n `6`; index avg `-0.2854` n `26`; metal avg `-0.984` n `20`; unknown avg `6.3165` n `815`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
