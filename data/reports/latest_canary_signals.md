# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T12:07:29.279247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1369` n `12`; crypto_alt avg `0.9395` n `234`; crypto_major avg `0.7494` n `8`; equity avg `0.2371` n `141`; fx avg `-0.0286` n `6`; index avg `0.0477` n `26`; metal avg `0.1349` n `20`; unknown avg `0.5856` n `954`
- 1h: commodity avg `-0.1101` n `12`; crypto_alt avg `1.029` n `234`; crypto_major avg `0.7611` n `8`; equity avg `0.3805` n `141`; fx avg `-0.0366` n `6`; index avg `0.0788` n `26`; metal avg `0.1417` n `20`; unknown avg `14.5829` n `954`
- 4h: commodity avg `0.1106` n `12`; crypto_alt avg `1.3051` n `234`; crypto_major avg `1.2516` n `8`; equity avg `0.0525` n `141`; fx avg `-0.0293` n `6`; index avg `0.0565` n `26`; metal avg `0.1152` n `20`; unknown avg `15.9002` n `952`
- 24h: commodity avg `-0.1713` n `12`; crypto_alt avg `-3.0172` n `234`; crypto_major avg `-2.1976` n `8`; equity avg `-2.3778` n `141`; fx avg `-0.0063` n `6`; index avg `-0.1865` n `26`; metal avg `-0.7828` n `20`; unknown avg `3.9718` n `814`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
