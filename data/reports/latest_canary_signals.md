# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T11:37:26.348023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0741` n `12`; crypto_alt avg `0.291` n `232`; crypto_major avg `0.1923` n `8`; equity avg `0.1059` n `130`; fx avg `-0.0044` n `6`; index avg `0.0181` n `26`; metal avg `0.0624` n `20`; unknown avg `0.1949` n `792`
- 1h: commodity avg `-0.0902` n `12`; crypto_alt avg `0.1468` n `232`; crypto_major avg `0.0035` n `8`; equity avg `-0.1539` n `130`; fx avg `0.0067` n `6`; index avg `-0.031` n `26`; metal avg `-0.0583` n `20`; unknown avg `-0.1782` n `790`
- 4h: commodity avg `-0.0481` n `12`; crypto_alt avg `-0.3728` n `232`; crypto_major avg `-0.2156` n `8`; equity avg `-1.3243` n `130`; fx avg `0.0283` n `6`; index avg `-0.2575` n `26`; metal avg `-0.4534` n `20`; unknown avg `-0.2093` n `790`
- 24h: commodity avg `0.0403` n `12`; crypto_alt avg `0.9986` n `232`; crypto_major avg `0.2146` n `8`; equity avg `-0.5985` n `130`; fx avg `0.1081` n `6`; index avg `-0.2443` n `26`; metal avg `-0.8042` n `20`; unknown avg `-0.123` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0374`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0291`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0288`, n `668`, weak_sample_signal
