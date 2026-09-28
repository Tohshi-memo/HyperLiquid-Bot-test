# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T20:07:32.715761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.057` n `12`; crypto_alt avg `0.4817` n `234`; crypto_major avg `0.1843` n `8`; equity avg `-0.069` n `141`; fx avg `0.002` n `6`; index avg `0.0052` n `26`; metal avg `-0.0428` n `20`; unknown avg `63.6139` n `923`
- 1h: commodity avg `0.105` n `12`; crypto_alt avg `-0.1784` n `234`; crypto_major avg `-0.2598` n `8`; equity avg `-0.2977` n `141`; fx avg `0.0004` n `6`; index avg `-0.0176` n `26`; metal avg `-0.0844` n `20`; unknown avg `17.851` n `885`
- 4h: commodity avg `-0.1444` n `12`; crypto_alt avg `0.2736` n `234`; crypto_major avg `-0.0189` n `8`; equity avg `0.0897` n `141`; fx avg `0.0113` n `6`; index avg `0.0616` n `26`; metal avg `-0.017` n `20`; unknown avg `26.5229` n `882`
- 24h: commodity avg `-0.2989` n `12`; crypto_alt avg `-3.9607` n `234`; crypto_major avg `-2.15` n `8`; equity avg `-3.4164` n `141`; fx avg `0.0443` n `6`; index avg `-0.3094` n `26`; metal avg `-1.1171` n `20`; unknown avg `26.437` n `776`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
