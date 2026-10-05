# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T12:07:41.209456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `13`; crypto_alt avg `-0.0457` n `235`; crypto_major avg `-0.0568` n `8`; equity avg `0.0464` n `144`; fx avg `-0.0069` n `6`; index avg `0.0051` n `26`; metal avg `0.0478` n `20`; unknown avg `-0.0441` n `1071`
- 1h: commodity avg `-0.0568` n `13`; crypto_alt avg `0.2342` n `235`; crypto_major avg `0.0577` n `8`; equity avg `0.101` n `144`; fx avg `0.0459` n `6`; index avg `0.0385` n `26`; metal avg `0.03` n `20`; unknown avg `0.4137` n `1071`
- 4h: commodity avg `0.1023` n `13`; crypto_alt avg `-0.3903` n `235`; crypto_major avg `-0.4287` n `8`; equity avg `-0.2677` n `144`; fx avg `0.0677` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0242` n `20`; unknown avg `45.6625` n `1053`
- 24h: commodity avg `-0.2258` n `13`; crypto_alt avg `1.0846` n `235`; crypto_major avg `0.896` n `8`; equity avg `0.0821` n `144`; fx avg `-0.0432` n `6`; index avg `-0.0398` n `26`; metal avg `0.2944` n `20`; unknown avg `0.7242` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2152`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1986`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
