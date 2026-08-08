# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T17:42:59.894194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.037` n `230`; crypto_major avg `0.0631` n `8`; equity avg `0.0643` n `112`; fx avg `-0.0007` n `6`; index avg `0.0066` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.0796` n `784`
- 1h: commodity avg `0.1058` n `12`; crypto_alt avg `0.0306` n `230`; crypto_major avg `0.1865` n `8`; equity avg `0.1414` n `112`; fx avg `0.0001` n `6`; index avg `0.012` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0668` n `784`
- 4h: commodity avg `0.0159` n `12`; crypto_alt avg `0.924` n `230`; crypto_major avg `0.7552` n `8`; equity avg `0.2137` n `112`; fx avg `-0.0022` n `6`; index avg `0.0101` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0152` n `784`
- 24h: commodity avg `-0.0929` n `12`; crypto_alt avg `1.7396` n `230`; crypto_major avg `2.0272` n `8`; equity avg `0.9687` n `112`; fx avg `0.0217` n `6`; index avg `0.0817` n `25`; metal avg `0.1453` n `20`; unknown avg `0.1405` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
