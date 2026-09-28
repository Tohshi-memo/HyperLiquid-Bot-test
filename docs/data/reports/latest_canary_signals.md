# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T11:22:28.943252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0531` n `12`; crypto_alt avg `0.0457` n `234`; crypto_major avg `0.0103` n `8`; equity avg `0.086` n `141`; fx avg `-0.0131` n `6`; index avg `0.0139` n `26`; metal avg `0.0244` n `20`; unknown avg `0.2271` n `962`
- 1h: commodity avg `-0.0506` n `12`; crypto_alt avg `0.5126` n `234`; crypto_major avg `0.4058` n `8`; equity avg `0.2363` n `141`; fx avg `-0.0138` n `6`; index avg `0.0353` n `26`; metal avg `-0.0005` n `20`; unknown avg `2.1883` n `960`
- 4h: commodity avg `0.1975` n `12`; crypto_alt avg `-0.023` n `234`; crypto_major avg `0.3694` n `8`; equity avg `-0.2364` n `141`; fx avg `-0.0697` n `6`; index avg `-0.0102` n `26`; metal avg `0.0603` n `20`; unknown avg `27.4163` n `942`
- 24h: commodity avg `-0.1014` n `12`; crypto_alt avg `-3.7412` n `234`; crypto_major avg `-2.6964` n `8`; equity avg `-2.6515` n `141`; fx avg `0.0169` n `6`; index avg `-0.2616` n `26`; metal avg `-0.8989` n `20`; unknown avg `8.2344` n `814`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
