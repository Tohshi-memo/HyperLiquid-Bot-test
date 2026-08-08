# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T19:42:20.013033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0136` n `230`; crypto_major avg `0.0133` n `8`; equity avg `0.1073` n `112`; fx avg `0.0103` n `6`; index avg `0.0086` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.0065` n `784`
- 1h: commodity avg `0.0343` n `12`; crypto_alt avg `-0.0435` n `230`; crypto_major avg `-0.0384` n `8`; equity avg `0.1594` n `112`; fx avg `0.0064` n `6`; index avg `0.011` n `25`; metal avg `0.0007` n `20`; unknown avg `0.3441` n `784`
- 4h: commodity avg `0.1172` n `12`; crypto_alt avg `0.2503` n `230`; crypto_major avg `-0.082` n `8`; equity avg `0.2997` n `112`; fx avg `0.0086` n `6`; index avg `-0.0039` n `25`; metal avg `0.0241` n `20`; unknown avg `0.4824` n `784`
- 24h: commodity avg `0.1624` n `12`; crypto_alt avg `1.413` n `230`; crypto_major avg `1.1432` n `8`; equity avg `0.9945` n `112`; fx avg `0.0313` n `6`; index avg `0.0445` n `25`; metal avg `0.0328` n `20`; unknown avg `0.1676` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
