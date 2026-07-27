# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T06:22:27.431374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1235` n `12`; crypto_alt avg `-0.1964` n `230`; crypto_major avg `-0.2069` n `8`; equity avg `0.0978` n `100`; fx avg `0.0186` n `6`; index avg `0.0031` n `25`; metal avg `-0.0134` n `20`; unknown avg `-0.0541` n `775`
- 1h: commodity avg `-0.1963` n `12`; crypto_alt avg `0.0104` n `230`; crypto_major avg `0.0904` n `8`; equity avg `0.1867` n `100`; fx avg `0.0082` n `6`; index avg `0.0319` n `25`; metal avg `0.0572` n `20`; unknown avg `-0.0415` n `759`
- 4h: commodity avg `-0.3891` n `12`; crypto_alt avg `0.1263` n `230`; crypto_major avg `0.453` n `8`; equity avg `0.6695` n `100`; fx avg `-0.0111` n `6`; index avg `0.1401` n `25`; metal avg `-0.0372` n `20`; unknown avg `-0.0277` n `759`
- 24h: commodity avg `-0.8487` n `12`; crypto_alt avg `1.3477` n `230`; crypto_major avg `1.8008` n `8`; equity avg `1.3087` n `100`; fx avg `0.0879` n `6`; index avg `0.1947` n `25`; metal avg `0.4051` n `20`; unknown avg `-0.0362` n `759`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
