# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T02:07:30.731338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1065` n `12`; crypto_alt avg `0.4489` n `232`; crypto_major avg `0.324` n `8`; equity avg `-0.0193` n `132`; fx avg `-0.0036` n `6`; index avg `0.0039` n `26`; metal avg `0.0195` n `20`; unknown avg `2.9341` n `790`
- 1h: commodity avg `-0.1068` n `12`; crypto_alt avg `-0.2049` n `232`; crypto_major avg `-0.3395` n `8`; equity avg `-0.3472` n `132`; fx avg `-0.0121` n `6`; index avg `-0.0626` n `26`; metal avg `-0.1486` n `20`; unknown avg `5.1024` n `790`
- 4h: commodity avg `0.0901` n `12`; crypto_alt avg `-0.4633` n `232`; crypto_major avg `-0.4409` n `8`; equity avg `-0.3148` n `132`; fx avg `-0.0612` n `6`; index avg `-0.0432` n `26`; metal avg `-0.2498` n `20`; unknown avg `0.1659` n `790`
- 24h: commodity avg `0.9627` n `12`; crypto_alt avg `-1.2711` n `232`; crypto_major avg `-2.0767` n `8`; equity avg `-2.4804` n `130`; fx avg `-0.0302` n `6`; index avg `-0.423` n `26`; metal avg `-1.1712` n `20`; unknown avg `-0.0343` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0391`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.037`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0316`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0301`, n `668`, weak_sample_signal
