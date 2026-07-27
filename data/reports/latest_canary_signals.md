# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T15:37:31.350567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5113` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.036` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.031` n `12`; crypto_alt avg `-0.44` n `230`; crypto_major avg `-0.3821` n `8`; equity avg `-0.6342` n `102`; fx avg `0.0021` n `6`; index avg `-0.1423` n `25`; metal avg `-0.066` n `20`; unknown avg `-0.3239` n `774`
- 1h: commodity avg `-0.0952` n `12`; crypto_alt avg `-0.122` n `230`; crypto_major avg `-0.01` n `8`; equity avg `0.0148` n `102`; fx avg `-0.0303` n `6`; index avg `-0.0842` n `25`; metal avg `0.1127` n `20`; unknown avg `-0.1333` n `774`
- 4h: commodity avg `0.0611` n `12`; crypto_alt avg `-1.9998` n `230`; crypto_major avg `-1.6644` n `8`; equity avg `-2.9972` n `102`; fx avg `-0.0665` n `6`; index avg `-0.6284` n `25`; metal avg `-0.1531` n `20`; unknown avg `-0.0776` n `774`
- 24h: commodity avg `-0.5729` n `12`; crypto_alt avg `-1.5924` n `230`; crypto_major avg `-0.964` n `8`; equity avg `-2.3188` n `102`; fx avg `0.0319` n `6`; index avg `-0.5341` n `25`; metal avg `0.2001` n `20`; unknown avg `-0.3957` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1923`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
