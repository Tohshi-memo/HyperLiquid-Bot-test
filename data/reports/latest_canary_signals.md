# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T23:39:57.059099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.493` n `234`; crypto_major avg `-0.1875` n `8`; equity avg `0.0304` n `142`; fx avg `-0.0077` n `6`; index avg `0.0138` n `26`; metal avg `-0.0025` n `20`; unknown avg `4.3199` n `963`
- 1h: commodity avg `-0.0646` n `12`; crypto_alt avg `-0.2943` n `234`; crypto_major avg `-0.0744` n `8`; equity avg `0.038` n `142`; fx avg `-0.0209` n `6`; index avg `0.0026` n `26`; metal avg `0.0212` n `20`; unknown avg `3.2686` n `960`
- 4h: commodity avg `0.0156` n `12`; crypto_alt avg `-0.6681` n `234`; crypto_major avg `-0.1013` n `8`; equity avg `0.2349` n `142`; fx avg `-0.0046` n `6`; index avg `0.0496` n `26`; metal avg `0.0734` n `20`; unknown avg `1.8993` n `872`
- 24h: commodity avg `-0.8979` n `12`; crypto_alt avg `-0.0718` n `234`; crypto_major avg `-0.3147` n `8`; equity avg `0.7486` n `142`; fx avg `-0.1444` n `6`; index avg `0.0984` n `26`; metal avg `0.2431` n `20`; unknown avg `3099.2367` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
