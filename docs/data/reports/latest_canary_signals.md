# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T11:37:25.350526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `0.0274` n `230`; crypto_major avg `-0.0107` n `8`; equity avg `-0.0034` n `112`; fx avg `-0.0022` n `6`; index avg `0.012` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0108` n `784`
- 1h: commodity avg `-0.0196` n `12`; crypto_alt avg `0.0412` n `230`; crypto_major avg `0.0256` n `8`; equity avg `0.0349` n `112`; fx avg `-0.0053` n `6`; index avg `0.0348` n `25`; metal avg `-0.0154` n `20`; unknown avg `-0.0722` n `784`
- 4h: commodity avg `0.0624` n `12`; crypto_alt avg `0.2713` n `230`; crypto_major avg `0.2543` n `8`; equity avg `0.2237` n `112`; fx avg `-0.0079` n `6`; index avg `0.0369` n `25`; metal avg `0.0134` n `20`; unknown avg `1.1739` n `784`
- 24h: commodity avg `0.2153` n `12`; crypto_alt avg `0.0334` n `230`; crypto_major avg `0.1217` n `8`; equity avg `0.7663` n `112`; fx avg `-0.0409` n `6`; index avg `0.0414` n `25`; metal avg `0.0337` n `20`; unknown avg `1.0528` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
