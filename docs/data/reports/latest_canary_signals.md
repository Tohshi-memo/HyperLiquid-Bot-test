# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T11:07:27.973742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `-0.1244` n `232`; crypto_major avg `-0.1189` n `8`; equity avg `-0.089` n `130`; fx avg `0.0023` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.0236` n `790`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.4643` n `232`; crypto_major avg `0.2902` n `8`; equity avg `-0.0869` n `130`; fx avg `0.0048` n `6`; index avg `-0.0095` n `26`; metal avg `0.0388` n `20`; unknown avg `0.1773` n `790`
- 4h: commodity avg `0.1282` n `12`; crypto_alt avg `-0.8481` n `232`; crypto_major avg `-0.7605` n `8`; equity avg `-1.4468` n `130`; fx avg `0.0254` n `6`; index avg `-0.3045` n `26`; metal avg `-0.5488` n `20`; unknown avg `-0.041` n `790`
- 24h: commodity avg `0.3174` n `12`; crypto_alt avg `0.532` n `232`; crypto_major avg `-0.2363` n `8`; equity avg `-0.7105` n `130`; fx avg `0.108` n `6`; index avg `-0.2688` n `26`; metal avg `-0.8159` n `20`; unknown avg `-0.0301` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0342`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0298`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0294`, n `668`, weak_sample_signal
