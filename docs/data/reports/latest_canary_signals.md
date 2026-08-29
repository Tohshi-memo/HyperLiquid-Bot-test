# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T20:52:29.362539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0559` n `231`; crypto_major avg `0.0017` n `8`; equity avg `-0.0011` n `128`; fx avg `-0.0035` n `6`; index avg `0.0001` n `26`; metal avg `-0.0039` n `20`; unknown avg `1.5506` n `792`
- 1h: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.0868` n `231`; crypto_major avg `-0.0748` n `8`; equity avg `0.0555` n `128`; fx avg `0.0064` n `6`; index avg `0.0062` n `26`; metal avg `0.0054` n `20`; unknown avg `-0.1182` n `792`
- 4h: commodity avg `-0.015` n `12`; crypto_alt avg `-0.2481` n `231`; crypto_major avg `-0.0966` n `8`; equity avg `0.184` n `128`; fx avg `-0.009` n `6`; index avg `0.0347` n `26`; metal avg `0.0195` n `20`; unknown avg `0.1416` n `792`
- 24h: commodity avg `-0.024` n `12`; crypto_alt avg `0.7005` n `231`; crypto_major avg `1.1076` n `8`; equity avg `0.3878` n `128`; fx avg `-0.0029` n `6`; index avg `0.0753` n `26`; metal avg `0.1393` n `20`; unknown avg `0.2017` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2296`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
