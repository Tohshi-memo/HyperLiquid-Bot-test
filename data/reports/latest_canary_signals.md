# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T15:56:03.373085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.1313` n `230`; crypto_major avg `0.0415` n `8`; equity avg `-0.0015` n `112`; fx avg `0.0073` n `6`; index avg `-0.0013` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.027` n `785`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `0.3327` n `230`; crypto_major avg `0.2607` n `8`; equity avg `-0.0033` n `112`; fx avg `0.0098` n `6`; index avg `0.007` n `25`; metal avg `0.0251` n `20`; unknown avg `0.0279` n `785`
- 4h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.738` n `230`; crypto_major avg `0.6095` n `8`; equity avg `0.0978` n `112`; fx avg `0.0131` n `6`; index avg `0.018` n `25`; metal avg `0.0487` n `20`; unknown avg `0.0915` n `785`
- 24h: commodity avg `0.1793` n `12`; crypto_alt avg `1.17` n `230`; crypto_major avg `0.2043` n `8`; equity avg `0.3184` n `112`; fx avg `0.0081` n `6`; index avg `0.0133` n `25`; metal avg `0.0728` n `20`; unknown avg `0.4286` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
