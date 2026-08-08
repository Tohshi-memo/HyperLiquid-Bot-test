# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T21:52:26.581678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `0.0411` n `230`; crypto_major avg `-0.0356` n `8`; equity avg `-0.0017` n `112`; fx avg `-0.0001` n `6`; index avg `0.002` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.0005` n `784`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `0.07` n `230`; crypto_major avg `-0.0013` n `8`; equity avg `0.0337` n `112`; fx avg `-0.0031` n `6`; index avg `-0.0073` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.1091` n `784`
- 4h: commodity avg `0.0264` n `12`; crypto_alt avg `0.0024` n `230`; crypto_major avg `-0.2011` n `8`; equity avg `0.1098` n `112`; fx avg `0.0029` n `6`; index avg `0.011` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.2765` n `784`
- 24h: commodity avg `0.21` n `12`; crypto_alt avg `1.8639` n `230`; crypto_major avg `1.3834` n `8`; equity avg `0.6827` n `112`; fx avg `-0.0014` n `6`; index avg `0.0361` n `25`; metal avg `0.0667` n `20`; unknown avg `0.1846` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal
