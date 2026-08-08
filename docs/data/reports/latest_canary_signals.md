# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T11:07:36.768322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0326` n `12`; crypto_alt avg `-0.0508` n `230`; crypto_major avg `0.0489` n `8`; equity avg `0.0174` n `112`; fx avg `0.0035` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0204` n `20`; unknown avg `0.007` n `784`
- 1h: commodity avg `0.0827` n `12`; crypto_alt avg `0.0213` n `230`; crypto_major avg `0.1005` n `8`; equity avg `0.0589` n `112`; fx avg `-0.0154` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0283` n `20`; unknown avg `-0.0465` n `784`
- 4h: commodity avg `0.1014` n `12`; crypto_alt avg `0.1629` n `230`; crypto_major avg `0.2869` n `8`; equity avg `0.1941` n `112`; fx avg `-0.0183` n `6`; index avg `-0.0004` n `25`; metal avg `0.0155` n `20`; unknown avg `1.3793` n `784`
- 24h: commodity avg `0.2025` n `12`; crypto_alt avg `0.0998` n `230`; crypto_major avg `0.135` n `8`; equity avg `0.7728` n `112`; fx avg `-0.0253` n `6`; index avg `0.0229` n `25`; metal avg `-0.0978` n `20`; unknown avg `1.1059` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
