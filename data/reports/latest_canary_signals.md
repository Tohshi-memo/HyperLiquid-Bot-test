# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T19:22:27.168579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `-0.0072` n `230`; crypto_major avg `0.0039` n `8`; equity avg `0.0607` n `112`; fx avg `-0.003` n `6`; index avg `0.0021` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0194` n `784`
- 1h: commodity avg `0.0513` n `12`; crypto_alt avg `-0.0454` n `230`; crypto_major avg `-0.1225` n `8`; equity avg `0.0519` n `112`; fx avg `-0.001` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0041` n `20`; unknown avg `0.4179` n `784`
- 4h: commodity avg `0.1317` n `12`; crypto_alt avg `0.359` n `230`; crypto_major avg `-0.1362` n `8`; equity avg `0.128` n `112`; fx avg `-0.0022` n `6`; index avg `0.0034` n `25`; metal avg `0.0157` n `20`; unknown avg `0.5326` n `784`
- 24h: commodity avg `0.1321` n `12`; crypto_alt avg `1.3528` n `230`; crypto_major avg `1.1345` n `8`; equity avg `0.6874` n `112`; fx avg `0.0134` n `6`; index avg `0.0144` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.1651` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
