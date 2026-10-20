# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T13:22:47.239331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0889` n `13`; crypto_alt avg `0.0514` n `237`; crypto_major avg `0.0774` n `8`; equity avg `-0.0403` n `151`; fx avg `0.021` n `6`; index avg `-0.0046` n `26`; metal avg `0.0352` n `20`; unknown avg `3.5164` n `1196`
- 1h: commodity avg `-0.0363` n `13`; crypto_alt avg `0.1138` n `237`; crypto_major avg `0.1924` n `8`; equity avg `0.4013` n `151`; fx avg `0.0288` n `6`; index avg `0.096` n `26`; metal avg `0.0819` n `20`; unknown avg `7.8367` n `1194`
- 4h: commodity avg `-0.0533` n `13`; crypto_alt avg `0.2319` n `237`; crypto_major avg `0.205` n `8`; equity avg `-0.087` n `151`; fx avg `0.0461` n `6`; index avg `0.0244` n `26`; metal avg `-0.0515` n `20`; unknown avg `4.7875` n `1186`
- 24h: commodity avg `0.3061` n `13`; crypto_alt avg `-0.0867` n `237`; crypto_major avg `-0.7259` n `8`; equity avg `-2.4653` n `151`; fx avg `0.0081` n `6`; index avg `-0.2923` n `26`; metal avg `-0.2181` n `20`; unknown avg `4.2892` n `1067`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
