# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T14:07:29.765145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.0886` n `230`; crypto_major avg `0.1314` n `8`; equity avg `0.0297` n `112`; fx avg `0.0045` n `6`; index avg `0.0015` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.0451` n `785`
- 1h: commodity avg `-0.0072` n `12`; crypto_alt avg `0.1369` n `230`; crypto_major avg `0.2947` n `8`; equity avg `0.0388` n `112`; fx avg `0.0076` n `6`; index avg `0.0089` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.013` n `785`
- 4h: commodity avg `-0.1304` n `12`; crypto_alt avg `0.4192` n `230`; crypto_major avg `0.386` n `8`; equity avg `0.1399` n `112`; fx avg `0.0006` n `6`; index avg `0.0226` n `25`; metal avg `0.0216` n `20`; unknown avg `0.0065` n `785`
- 24h: commodity avg `0.0675` n `12`; crypto_alt avg `1.3724` n `230`; crypto_major avg `0.4572` n `8`; equity avg `0.3304` n `112`; fx avg `-0.0103` n `6`; index avg `0.0383` n `25`; metal avg `0.0579` n `20`; unknown avg `0.3898` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
