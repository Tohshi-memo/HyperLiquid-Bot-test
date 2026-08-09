# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T15:52:21.469180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `0.1247` n `230`; crypto_major avg `-0.0124` n `8`; equity avg `-0.0042` n `112`; fx avg `0.0079` n `6`; index avg `0.0026` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.0026` n `785`
- 1h: commodity avg `0.0043` n `12`; crypto_alt avg `0.3263` n `230`; crypto_major avg `0.2065` n `8`; equity avg `-0.0061` n `112`; fx avg `0.0104` n `6`; index avg `0.0109` n `25`; metal avg `0.0255` n `20`; unknown avg `0.0398` n `785`
- 4h: commodity avg `-0.0102` n `12`; crypto_alt avg `0.7293` n `230`; crypto_major avg `0.5552` n `8`; equity avg `0.095` n `112`; fx avg `0.0137` n `6`; index avg `0.022` n `25`; metal avg `0.0491` n `20`; unknown avg `0.0981` n `785`
- 24h: commodity avg `0.1779` n `12`; crypto_alt avg `1.1608` n `230`; crypto_major avg `0.15` n `8`; equity avg `0.3156` n `112`; fx avg `0.0088` n `6`; index avg `0.0172` n `25`; metal avg `0.0732` n `20`; unknown avg `0.4282` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
