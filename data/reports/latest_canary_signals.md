# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T23:07:29.425681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `0.4986` n `234`; crypto_major avg `0.2212` n `8`; equity avg `-0.0022` n `142`; fx avg `-0.0037` n `6`; index avg `-0.0099` n `26`; metal avg `0.0084` n `20`; unknown avg `0.0753` n `961`
- 1h: commodity avg `0.1771` n `12`; crypto_alt avg `0.2713` n `234`; crypto_major avg `0.2728` n `8`; equity avg `-0.0075` n `142`; fx avg `0.0001` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0117` n `20`; unknown avg `0.668` n `960`
- 4h: commodity avg `0.0495` n `12`; crypto_alt avg `-0.0891` n `234`; crypto_major avg `-0.0027` n `8`; equity avg `0.0644` n `142`; fx avg `0.0089` n `6`; index avg `0.0235` n `26`; metal avg `0.0737` n `20`; unknown avg `-0.2987` n `872`
- 24h: commodity avg `-0.8684` n `12`; crypto_alt avg `1.0772` n `234`; crypto_major avg `0.1403` n `8`; equity avg `0.7453` n `142`; fx avg `-0.1749` n `6`; index avg `0.0887` n `26`; metal avg `0.2684` n `20`; unknown avg `3099.1881` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
