# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T19:37:34.487818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.0246` n `230`; crypto_major avg `0.0069` n `8`; equity avg `0.0828` n `112`; fx avg `0.0095` n `6`; index avg `0.0055` n `25`; metal avg `0.005` n `20`; unknown avg `0.0052` n `784`
- 1h: commodity avg `0.0534` n `12`; crypto_alt avg `-0.0327` n `230`; crypto_major avg `-0.0448` n `8`; equity avg `0.1349` n `112`; fx avg `0.0056` n `6`; index avg `0.0079` n `25`; metal avg `-0.0029` n `20`; unknown avg `0.354` n `784`
- 4h: commodity avg `0.1365` n `12`; crypto_alt avg `0.2613` n `230`; crypto_major avg `-0.0884` n `8`; equity avg `0.275` n `112`; fx avg `0.0077` n `6`; index avg `-0.0069` n `25`; metal avg `0.0205` n `20`; unknown avg `0.4963` n `784`
- 24h: commodity avg `0.1817` n `12`; crypto_alt avg `1.423` n `230`; crypto_major avg `1.1367` n `8`; equity avg `0.9693` n `112`; fx avg `0.0304` n `6`; index avg `0.0414` n `25`; metal avg `0.0292` n `20`; unknown avg `0.1869` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
