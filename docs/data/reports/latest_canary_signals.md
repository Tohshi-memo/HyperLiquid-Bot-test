# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T12:37:28.214230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0711` n `12`; crypto_alt avg `0.0139` n `234`; crypto_major avg `0.0498` n `8`; equity avg `-0.0288` n `141`; fx avg `0.0272` n `6`; index avg `0.0001` n `26`; metal avg `-0.1347` n `20`; unknown avg `0.3978` n `962`
- 1h: commodity avg `-0.1746` n `12`; crypto_alt avg `1.0368` n `234`; crypto_major avg `0.5302` n `8`; equity avg `0.1184` n `141`; fx avg `0.0194` n `6`; index avg `0.0429` n `26`; metal avg `-0.0165` n `20`; unknown avg `884.2085` n `954`
- 4h: commodity avg `-0.0628` n `12`; crypto_alt avg `1.4064` n `234`; crypto_major avg `1.1736` n `8`; equity avg `0.3129` n `141`; fx avg `0.0412` n `6`; index avg `0.0675` n `26`; metal avg `0.0714` n `20`; unknown avg `275.248` n `952`
- 24h: commodity avg `-0.2634` n `12`; crypto_alt avg `-2.7929` n `234`; crypto_major avg `-2.3054` n `8`; equity avg `-2.4555` n `141`; fx avg `0.0262` n `6`; index avg `-0.1876` n `26`; metal avg `-0.9211` n `20`; unknown avg `4.3037` n `814`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
