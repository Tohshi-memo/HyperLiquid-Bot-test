# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T19:22:32.433303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1898` n `12`; crypto_alt avg `-0.2593` n `234`; crypto_major avg `-0.2145` n `8`; equity avg `-0.0394` n `141`; fx avg `-0.0085` n `6`; index avg `-0.0068` n `26`; metal avg `0.0139` n `20`; unknown avg `-0.3065` n `925`
- 1h: commodity avg `0.2761` n `12`; crypto_alt avg `-0.9961` n `234`; crypto_major avg `-0.6988` n `8`; equity avg `-0.151` n `141`; fx avg `-0.0053` n `6`; index avg `-0.036` n `26`; metal avg `-0.0585` n `20`; unknown avg `0.5063` n `921`
- 4h: commodity avg `-0.2116` n `12`; crypto_alt avg `1.1749` n `234`; crypto_major avg `0.8187` n `8`; equity avg `0.8077` n `141`; fx avg `-0.0264` n `6`; index avg `0.1242` n `26`; metal avg `0.0878` n `20`; unknown avg `16.1925` n `914`
- 24h: commodity avg `-0.209` n `12`; crypto_alt avg `-4.0301` n `234`; crypto_major avg `-2.195` n `8`; equity avg `-3.1353` n `141`; fx avg `0.0353` n `6`; index avg `-0.2945` n `26`; metal avg `-1.0223` n `20`; unknown avg `25.7589` n `806`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
