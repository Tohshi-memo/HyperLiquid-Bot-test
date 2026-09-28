# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T19:37:32.007939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1189` n `12`; crypto_alt avg `-0.4662` n `234`; crypto_major avg `-0.4123` n `8`; equity avg `-0.0963` n `141`; fx avg `0.0036` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0073` n `20`; unknown avg `12.236` n `963`
- 1h: commodity avg `0.1456` n `12`; crypto_alt avg `-1.1226` n `234`; crypto_major avg `-0.9408` n `8`; equity avg `-0.1753` n `141`; fx avg `-0.0022` n `6`; index avg `-0.0302` n `26`; metal avg `-0.0387` n `20`; unknown avg `11.8634` n `921`
- 4h: commodity avg `-0.3591` n `12`; crypto_alt avg `-0.0615` n `234`; crypto_major avg `-0.1626` n `8`; equity avg `0.4698` n `141`; fx avg `-0.0103` n `6`; index avg `0.0744` n `26`; metal avg `0.0519` n `20`; unknown avg `29.302` n `914`
- 24h: commodity avg `-0.3055` n `12`; crypto_alt avg `-4.3568` n `234`; crypto_major avg `-2.5383` n `8`; equity avg `-3.2374` n `141`; fx avg `0.0385` n `6`; index avg `-0.3036` n `26`; metal avg `-1.031` n `20`; unknown avg `32.7529` n `806`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
