# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T14:22:28.936729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0764` n `12`; crypto_alt avg `-0.0844` n `232`; crypto_major avg `-0.1659` n `8`; equity avg `0.0469` n `131`; fx avg `-0.0054` n `6`; index avg `0.023` n `26`; metal avg `0.0753` n `20`; unknown avg `-0.058` n `792`
- 1h: commodity avg `-0.0824` n `12`; crypto_alt avg `0.6342` n `232`; crypto_major avg `0.394` n `8`; equity avg `-0.3056` n `131`; fx avg `-0.0063` n `6`; index avg `0.0607` n `26`; metal avg `0.2458` n `20`; unknown avg `0.4224` n `790`
- 4h: commodity avg `-0.1395` n `12`; crypto_alt avg `0.6611` n `232`; crypto_major avg `0.1711` n `8`; equity avg `-0.8541` n `130`; fx avg `-0.0135` n `6`; index avg `-0.0261` n `26`; metal avg `-0.0255` n `20`; unknown avg `-0.244` n `790`
- 24h: commodity avg `0.2693` n `12`; crypto_alt avg `1.7018` n `232`; crypto_major avg `0.6687` n `8`; equity avg `-1.2556` n `130`; fx avg `0.0568` n `6`; index avg `-0.1818` n `26`; metal avg `-0.429` n `20`; unknown avg `0.6264` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0395`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0316`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0307`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0301`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.03`, n `668`, weak_sample_signal
