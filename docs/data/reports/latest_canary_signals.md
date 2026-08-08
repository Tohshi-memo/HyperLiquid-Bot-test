# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T23:25:22.523231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `0.0638` n `230`; crypto_major avg `0.0388` n `8`; equity avg `-0.0113` n `112`; fx avg `-0.0004` n `6`; index avg `0.0065` n `25`; metal avg `0.0105` n `20`; unknown avg `0.0405` n `784`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `-0.0628` n `230`; crypto_major avg `-0.1237` n `8`; equity avg `0.0022` n `112`; fx avg `0.0038` n `6`; index avg `0.0097` n `25`; metal avg `0.0161` n `20`; unknown avg `-0.0403` n `784`
- 4h: commodity avg `0.0144` n `12`; crypto_alt avg `0.0197` n `230`; crypto_major avg `-0.1869` n `8`; equity avg `0.0718` n `112`; fx avg `0.0065` n `6`; index avg `0.0185` n `25`; metal avg `0.0185` n `20`; unknown avg `-0.1904` n `784`
- 24h: commodity avg `0.1644` n `12`; crypto_alt avg `1.7711` n `230`; crypto_major avg `1.157` n `8`; equity avg `0.6366` n `112`; fx avg `-0.0122` n `6`; index avg `0.034` n `25`; metal avg `0.0264` n `20`; unknown avg `0.1812` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
