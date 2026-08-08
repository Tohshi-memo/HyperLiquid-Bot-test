# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T22:07:28.276859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0164` n `230`; crypto_major avg `-0.0746` n `8`; equity avg `-0.0151` n `112`; fx avg `-0.0017` n `6`; index avg `0.0002` n `25`; metal avg `0.0065` n `20`; unknown avg `0.0108` n `784`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `0.0421` n `230`; crypto_major avg `-0.0909` n `8`; equity avg `-0.0021` n `112`; fx avg `-0.0009` n `6`; index avg `-0.0141` n `25`; metal avg `0.0084` n `20`; unknown avg `-0.0928` n `784`
- 4h: commodity avg `0.0509` n `12`; crypto_alt avg `0.0676` n `230`; crypto_major avg `-0.1658` n `8`; equity avg `0.1214` n `112`; fx avg `0.0014` n `6`; index avg `0.0099` n `25`; metal avg `0.0019` n `20`; unknown avg `0.2762` n `784`
- 24h: commodity avg `0.2024` n `12`; crypto_alt avg `1.9206` n `230`; crypto_major avg `1.3266` n `8`; equity avg `0.6499` n `112`; fx avg `-0.0212` n `6`; index avg `0.0344` n `25`; metal avg `0.0455` n `20`; unknown avg `0.2083` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
