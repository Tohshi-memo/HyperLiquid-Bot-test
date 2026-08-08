# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T18:37:29.818378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `0.0117` n `230`; crypto_major avg `-0.0707` n `8`; equity avg `0.0001` n `112`; fx avg `0.0029` n `6`; index avg `-0.0034` n `25`; metal avg `0.0038` n `20`; unknown avg `0.4509` n `784`
- 1h: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.0681` n `230`; crypto_major avg `-0.2739` n `8`; equity avg `-0.0222` n `112`; fx avg `0.0028` n `6`; index avg `-0.001` n `25`; metal avg `0.0124` n `20`; unknown avg `0.5342` n `784`
- 4h: commodity avg `0.0294` n `12`; crypto_alt avg `0.4709` n `230`; crypto_major avg `-0.1451` n `8`; equity avg `0.1463` n `112`; fx avg `0.0039` n `6`; index avg `0.0084` n `25`; metal avg `0.0169` n `20`; unknown avg `0.3938` n `784`
- 24h: commodity avg `-0.143` n `12`; crypto_alt avg `1.6057` n `230`; crypto_major avg `1.5779` n `8`; equity avg `1.0337` n `112`; fx avg `0.0107` n `6`; index avg `0.1094` n `25`; metal avg `0.1028` n `20`; unknown avg `0.1419` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
