# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T10:07:33.088956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `-0.0418` n `230`; crypto_major avg `0.0501` n `8`; equity avg `-0.0402` n `112`; fx avg `-0.0009` n `6`; index avg `-0.0076` n `25`; metal avg `-0.0122` n `20`; unknown avg `0.0792` n `785`
- 1h: commodity avg `0.0609` n `12`; crypto_alt avg `0.0932` n `230`; crypto_major avg `0.075` n `8`; equity avg `-0.0791` n `112`; fx avg `-0.0009` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.0466` n `785`
- 4h: commodity avg `0.0673` n `12`; crypto_alt avg `-0.0414` n `230`; crypto_major avg `0.0806` n `8`; equity avg `-0.1002` n `112`; fx avg `-0.013` n `6`; index avg `-0.0202` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0385` n `784`
- 24h: commodity avg `0.3224` n `12`; crypto_alt avg `1.1968` n `230`; crypto_major avg `0.3341` n `8`; equity avg `0.4378` n `112`; fx avg `-0.0218` n `6`; index avg `0.0478` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.1902` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.043`, n `668`, weak_sample_signal
