# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T20:52:25.770683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.0041` n `230`; crypto_major avg `-0.0143` n `8`; equity avg `-0.007` n `112`; fx avg `0.0042` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.0004` n `784`
- 1h: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.025` n `230`; crypto_major avg `0.0141` n `8`; equity avg `-0.0218` n `112`; fx avg `-0.0023` n `6`; index avg `0.0089` n `25`; metal avg `-0.0073` n `20`; unknown avg `-0.0232` n `784`
- 4h: commodity avg `0.111` n `12`; crypto_alt avg `-0.0403` n `230`; crypto_major avg `-0.1744` n `8`; equity avg `0.1834` n `112`; fx avg `0.0031` n `6`; index avg `0.0197` n `25`; metal avg `-0.0182` n `20`; unknown avg `0.2982` n `784`
- 24h: commodity avg `0.1159` n `12`; crypto_alt avg `1.7042` n `230`; crypto_major avg `1.2876` n `8`; equity avg `0.6311` n `112`; fx avg `0.0187` n `6`; index avg `0.0273` n `25`; metal avg `0.1014` n `20`; unknown avg `0.1907` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
