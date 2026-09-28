# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T21:07:31.747785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0218` n `12`; crypto_alt avg `0.3036` n `234`; crypto_major avg `0.158` n `8`; equity avg `0.0729` n `141`; fx avg `0.0131` n `6`; index avg `0.0153` n `26`; metal avg `0.0221` n `20`; unknown avg `0.8329` n `959`
- 1h: commodity avg `0.0653` n `12`; crypto_alt avg `0.0675` n `234`; crypto_major avg `0.0178` n `8`; equity avg `0.061` n `141`; fx avg `0.0033` n `6`; index avg `0.0009` n `26`; metal avg `-0.0423` n `20`; unknown avg `-0.7269` n `917`
- 4h: commodity avg `0.0982` n `12`; crypto_alt avg `0.2718` n `234`; crypto_major avg `-0.0708` n `8`; equity avg `-0.0243` n `141`; fx avg `0.0006` n `6`; index avg `0.0057` n `26`; metal avg `-0.1292` n `20`; unknown avg `1.9825` n `856`
- 24h: commodity avg `-0.2633` n `12`; crypto_alt avg `-3.4944` n `234`; crypto_major avg `-1.9697` n `8`; equity avg `-3.3315` n `141`; fx avg `0.1025` n `6`; index avg `-0.3048` n `26`; metal avg `-1.1513` n `20`; unknown avg `26.6813` n `776`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
