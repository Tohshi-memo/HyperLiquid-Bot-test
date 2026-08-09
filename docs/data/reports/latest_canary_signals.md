# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T23:59:47.361640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `0.0377` n `230`; crypto_major avg `-0.0277` n `8`; equity avg `-0.0035` n `112`; fx avg `0.0056` n `6`; index avg `0.0059` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.0704` n `784`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.0406` n `230`; crypto_major avg `-0.0109` n `8`; equity avg `-0.0318` n `112`; fx avg `0.0011` n `6`; index avg `0.0142` n `25`; metal avg `0.0346` n `20`; unknown avg `-0.0587` n `784`
- 4h: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.0418` n `230`; crypto_major avg `-0.2443` n `8`; equity avg `-0.0141` n `112`; fx avg `0.0003` n `6`; index avg `0.0183` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.2011` n `784`
- 24h: commodity avg `0.1777` n `12`; crypto_alt avg `1.8382` n `230`; crypto_major avg `1.1877` n `8`; equity avg `0.5314` n `112`; fx avg `-0.0039` n `6`; index avg `0.0548` n `25`; metal avg `0.0407` n `20`; unknown avg `0.19` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
