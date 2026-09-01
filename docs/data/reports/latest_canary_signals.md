# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T04:07:27.417770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.0572` n `232`; crypto_major avg `-0.0519` n `8`; equity avg `0.0271` n `130`; fx avg `-0.0039` n `6`; index avg `0.0067` n `26`; metal avg `-0.0677` n `20`; unknown avg `-0.1901` n `790`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `0.2723` n `232`; crypto_major avg `0.3473` n `8`; equity avg `0.1769` n `130`; fx avg `0.0265` n `6`; index avg `0.0173` n `26`; metal avg `-0.0043` n `20`; unknown avg `-0.2737` n `790`
- 4h: commodity avg `-0.0427` n `12`; crypto_alt avg `0.5327` n `232`; crypto_major avg `0.135` n `8`; equity avg `0.1702` n `130`; fx avg `0.018` n `6`; index avg `0.0587` n `26`; metal avg `-0.1086` n `20`; unknown avg `0.4662` n `790`
- 24h: commodity avg `0.3904` n `12`; crypto_alt avg `1.8763` n `232`; crypto_major avg `1.9719` n `8`; equity avg `1.4177` n `130`; fx avg `0.0135` n `6`; index avg `0.1502` n `26`; metal avg `0.0406` n `20`; unknown avg `0.1451` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
