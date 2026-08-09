# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T03:22:28.823950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.0859` n `230`; crypto_major avg `0.0154` n `8`; equity avg `-0.1021` n `112`; fx avg `0.0006` n `6`; index avg `-0.0037` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.0387` n `784`
- 1h: commodity avg `0.0098` n `12`; crypto_alt avg `-0.1356` n `230`; crypto_major avg `-0.1234` n `8`; equity avg `-0.0517` n `112`; fx avg `0.0083` n `6`; index avg `-0.0019` n `25`; metal avg `0.0154` n `20`; unknown avg `-0.0077` n `784`
- 4h: commodity avg `0.0395` n `12`; crypto_alt avg `-0.0392` n `230`; crypto_major avg `-0.2063` n `8`; equity avg `-0.069` n `112`; fx avg `0.0105` n `6`; index avg `-0.011` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.2074` n `784`
- 24h: commodity avg `0.2022` n `12`; crypto_alt avg `1.4789` n `230`; crypto_major avg `0.631` n `8`; equity avg `0.4353` n `112`; fx avg `0.0025` n `6`; index avg `0.0278` n `25`; metal avg `0.0268` n `20`; unknown avg `-0.021` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
