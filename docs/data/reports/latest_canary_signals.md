# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T12:07:25.665387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `0.0821` n `230`; crypto_major avg `-0.0264` n `8`; equity avg `-0.0033` n `112`; fx avg `-0.0063` n `6`; index avg `-0.0217` n `25`; metal avg `-0.0167` n `20`; unknown avg `-0.0029` n `784`
- 1h: commodity avg `-0.0209` n `12`; crypto_alt avg `0.1362` n `230`; crypto_major avg `-0.0191` n `8`; equity avg `0.0123` n `112`; fx avg `0.0012` n `6`; index avg `0.0063` n `25`; metal avg `-0.012` n `20`; unknown avg `-0.0047` n `784`
- 4h: commodity avg `0.061` n `12`; crypto_alt avg `0.2961` n `230`; crypto_major avg `0.2752` n `8`; equity avg `0.1761` n `112`; fx avg `-0.0128` n `6`; index avg `-0.0011` n `25`; metal avg `0.0017` n `20`; unknown avg `1.2574` n `784`
- 24h: commodity avg `0.1953` n `12`; crypto_alt avg `0.0815` n `230`; crypto_major avg `-0.0126` n `8`; equity avg `0.7677` n `112`; fx avg `-0.0471` n `6`; index avg `0.006` n `25`; metal avg `0.0442` n `20`; unknown avg `1.0523` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
