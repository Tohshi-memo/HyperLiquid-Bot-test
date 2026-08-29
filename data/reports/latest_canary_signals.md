# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T20:22:24.975086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.018` n `231`; crypto_major avg `-0.0595` n `8`; equity avg `0.0247` n `128`; fx avg `0.0011` n `6`; index avg `-0.0018` n `26`; metal avg `0.0039` n `20`; unknown avg `0.3543` n `792`
- 1h: commodity avg `-0.011` n `12`; crypto_alt avg `-0.0389` n `231`; crypto_major avg `-0.0615` n `8`; equity avg `0.1179` n `128`; fx avg `-0.0014` n `6`; index avg `0.0213` n `26`; metal avg `0.0022` n `20`; unknown avg `1.195` n `792`
- 4h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.07` n `231`; crypto_major avg `0.2349` n `8`; equity avg `0.179` n `128`; fx avg `-0.0131` n `6`; index avg `0.029` n `26`; metal avg `0.0281` n `20`; unknown avg `-0.2135` n `792`
- 24h: commodity avg `-0.0126` n `12`; crypto_alt avg `0.8192` n `231`; crypto_major avg `1.2397` n `8`; equity avg `0.4055` n `128`; fx avg `-0.043` n `6`; index avg `0.0898` n `26`; metal avg `0.1734` n `20`; unknown avg `0.2085` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2304`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
