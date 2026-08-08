# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T13:30:06.335378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.0249` n `230`; crypto_major avg `0.0058` n `8`; equity avg `-0.0392` n `112`; fx avg `0.0006` n `6`; index avg `-0.0123` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.021` n `784`
- 1h: commodity avg `0.0356` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.0222` n `8`; equity avg `0.1373` n `112`; fx avg `-0.0033` n `6`; index avg `0.022` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.126` n `784`
- 4h: commodity avg `0.0943` n `12`; crypto_alt avg `0.244` n `230`; crypto_major avg `0.1475` n `8`; equity avg `0.2268` n `112`; fx avg `-0.0152` n `6`; index avg `0.0376` n `25`; metal avg `-0.0275` n `20`; unknown avg `-0.1097` n `784`
- 24h: commodity avg `0.0612` n `12`; crypto_alt avg `0.2436` n `230`; crypto_major avg `-0.0615` n `8`; equity avg `0.6287` n `112`; fx avg `0.0075` n `6`; index avg `-0.0266` n `25`; metal avg `-0.0793` n `20`; unknown avg `-0.1579` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
