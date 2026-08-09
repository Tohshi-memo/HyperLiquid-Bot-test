# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T05:22:29.785463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `-0.2285` n `230`; crypto_major avg `-0.042` n `8`; equity avg `-0.0025` n `112`; fx avg `-0.0055` n `6`; index avg `-0.0044` n `25`; metal avg `0.0036` n `20`; unknown avg `0.7586` n `784`
- 1h: commodity avg `-0.005` n `12`; crypto_alt avg `-0.3189` n `230`; crypto_major avg `-0.1093` n `8`; equity avg `0.0262` n `112`; fx avg `-0.0014` n `6`; index avg `0.0065` n `25`; metal avg `-0.006` n `20`; unknown avg `0.7527` n `784`
- 4h: commodity avg `0.086` n `12`; crypto_alt avg `-0.0086` n `230`; crypto_major avg `-0.2287` n `8`; equity avg `-0.0833` n `112`; fx avg `0.0021` n `6`; index avg `-0.003` n `25`; metal avg `-0.0101` n `20`; unknown avg `0.1445` n `784`
- 24h: commodity avg `0.2931` n `12`; crypto_alt avg `1.4226` n `230`; crypto_major avg `0.4562` n `8`; equity avg `0.5605` n `112`; fx avg `-0.0071` n `6`; index avg `0.0723` n `25`; metal avg `0.0279` n `20`; unknown avg `-0.0164` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
