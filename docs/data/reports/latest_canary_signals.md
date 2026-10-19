# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T22:37:33.687036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `13`; crypto_alt avg `-0.1149` n `237`; crypto_major avg `-0.1546` n `8`; equity avg `-0.0008` n `151`; fx avg `0.0034` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0275` n `20`; unknown avg `1.0974` n `1196`
- 1h: commodity avg `-0.0244` n `13`; crypto_alt avg `0.6987` n `237`; crypto_major avg `0.2661` n `8`; equity avg `0.1131` n `151`; fx avg `-0.0111` n `6`; index avg `0.0344` n `26`; metal avg `-0.0297` n `20`; unknown avg `1.5651` n `1184`
- 4h: commodity avg `-0.0868` n `13`; crypto_alt avg `1.0841` n `237`; crypto_major avg `0.6839` n `8`; equity avg `0.389` n `151`; fx avg `-0.0032` n `6`; index avg `0.062` n `26`; metal avg `-0.0703` n `20`; unknown avg `3.1697` n `1114`
- 24h: commodity avg `0.0026` n `13`; crypto_alt avg `1.7669` n `237`; crypto_major avg `1.013` n `8`; equity avg `1.7589` n `151`; fx avg `-0.0358` n `6`; index avg `0.3262` n `26`; metal avg `-0.1724` n `20`; unknown avg `3.3869` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
