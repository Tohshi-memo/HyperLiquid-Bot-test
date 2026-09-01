# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T05:07:27.964666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `0.1144` n `232`; crypto_major avg `0.1161` n `8`; equity avg `-0.0122` n `130`; fx avg `-0.0273` n `6`; index avg `-0.0082` n `26`; metal avg `0.0295` n `20`; unknown avg `-0.257` n `790`
- 1h: commodity avg `0.1028` n `12`; crypto_alt avg `0.1386` n `232`; crypto_major avg `0.0504` n `8`; equity avg `0.022` n `130`; fx avg `-0.0142` n `6`; index avg `-0.0121` n `26`; metal avg `-0.0173` n `20`; unknown avg `0.2438` n `790`
- 4h: commodity avg `0.0875` n `12`; crypto_alt avg `0.3169` n `232`; crypto_major avg `0.1955` n `8`; equity avg `0.0456` n `130`; fx avg `0.0023` n `6`; index avg `-0.0191` n `26`; metal avg `-0.1243` n `20`; unknown avg `0.3942` n `790`
- 24h: commodity avg `0.419` n `12`; crypto_alt avg `2.1083` n `232`; crypto_major avg `1.974` n `8`; equity avg `0.976` n `130`; fx avg `-0.027` n `6`; index avg `0.0209` n `26`; metal avg `-0.061` n `20`; unknown avg `0.4545` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
