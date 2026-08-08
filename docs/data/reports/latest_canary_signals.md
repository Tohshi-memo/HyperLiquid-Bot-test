# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T16:57:48.164885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `0.0028` n `230`; crypto_major avg `0.1389` n `8`; equity avg `0.0397` n `112`; fx avg `0.0003` n `6`; index avg `0.0084` n `25`; metal avg `0.0272` n `20`; unknown avg `-0.0078` n `784`
- 1h: commodity avg `0.0271` n `12`; crypto_alt avg `0.285` n `230`; crypto_major avg `0.1067` n `8`; equity avg `0.0512` n `112`; fx avg `0.0053` n `6`; index avg `-0.0066` n `25`; metal avg `0.0166` n `20`; unknown avg `0.0589` n `784`
- 4h: commodity avg `-0.0216` n `12`; crypto_alt avg `0.895` n `230`; crypto_major avg `0.648` n `8`; equity avg `0.2169` n `112`; fx avg `-0.0096` n `6`; index avg `0.0278` n `25`; metal avg `0.0289` n `20`; unknown avg `-0.1747` n `784`
- 24h: commodity avg `-0.2504` n `12`; crypto_alt avg `1.4813` n `230`; crypto_major avg `1.3426` n `8`; equity avg `0.7688` n `112`; fx avg `0.0128` n `6`; index avg `0.0595` n `25`; metal avg `0.1856` n `20`; unknown avg `0.1464` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
