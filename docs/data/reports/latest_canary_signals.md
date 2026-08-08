# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T23:22:27.644889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `0.0359` n `230`; crypto_major avg `0.0126` n `8`; equity avg `-0.0185` n `112`; fx avg `-0.0017` n `6`; index avg `0.0066` n `25`; metal avg `0.0097` n `20`; unknown avg `0.0623` n `784`
- 1h: commodity avg `0.0105` n `12`; crypto_alt avg `-0.0908` n `230`; crypto_major avg `-0.1499` n `8`; equity avg `-0.0051` n `112`; fx avg `0.0025` n `6`; index avg `0.0098` n `25`; metal avg `0.0153` n `20`; unknown avg `-0.0203` n `784`
- 4h: commodity avg `0.017` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `-0.2131` n `8`; equity avg `0.0646` n `112`; fx avg `0.0053` n `6`; index avg `0.0186` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.1778` n `784`
- 24h: commodity avg `0.1671` n `12`; crypto_alt avg `1.7422` n `230`; crypto_major avg `1.1304` n `8`; equity avg `0.6292` n `112`; fx avg `-0.0134` n `6`; index avg `0.034` n `25`; metal avg `0.0256` n `20`; unknown avg `0.1885` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
