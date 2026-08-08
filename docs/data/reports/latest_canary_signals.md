# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T17:07:27.693897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1159` n `12`; crypto_alt avg `-0.0033` n `230`; crypto_major avg `-0.0586` n `8`; equity avg `0.0181` n `112`; fx avg `-0.0022` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.0337` n `784`
- 1h: commodity avg `0.1464` n `12`; crypto_alt avg `0.1636` n `230`; crypto_major avg `-0.0599` n `8`; equity avg `0.0894` n `112`; fx avg `0.001` n `6`; index avg `-0.0091` n `25`; metal avg `0.025` n `20`; unknown avg `0.0204` n `784`
- 4h: commodity avg `0.0835` n `12`; crypto_alt avg `0.8678` n `230`; crypto_major avg `0.548` n `8`; equity avg `0.2488` n `112`; fx avg `-0.0055` n `6`; index avg `0.0262` n `25`; metal avg `0.0225` n `20`; unknown avg `-0.1965` n `784`
- 24h: commodity avg `-0.0814` n `12`; crypto_alt avg `1.6699` n `230`; crypto_major avg `1.7321` n `8`; equity avg `0.9131` n `112`; fx avg `0.0125` n `6`; index avg `0.0616` n `25`; metal avg `0.1645` n `20`; unknown avg `0.1503` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
