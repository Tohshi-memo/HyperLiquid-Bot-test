# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T22:52:25.788993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.1551` n `230`; crypto_major avg `-0.0809` n `8`; equity avg `-0.1932` n `94`; fx avg `0.007` n `6`; index avg `-0.0054` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.0602` n `768`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.753` n `230`; crypto_major avg `-0.568` n `8`; equity avg `-0.5028` n `94`; fx avg `-0.0049` n `6`; index avg `-0.0616` n `25`; metal avg `-0.0732` n `20`; unknown avg `-0.2614` n `768`
- 4h: commodity avg `0.1567` n `12`; crypto_alt avg `-0.6116` n `230`; crypto_major avg `-0.5098` n `8`; equity avg `-0.5846` n `94`; fx avg `-0.0108` n `6`; index avg `-0.037` n `25`; metal avg `-0.0862` n `20`; unknown avg `-0.3688` n `768`
- 24h: commodity avg `-0.195` n `12`; crypto_alt avg `-1.6398` n `230`; crypto_major avg `-2.5602` n `8`; equity avg `-3.997` n `94`; fx avg `-0.1633` n `6`; index avg `-0.525` n `25`; metal avg `-0.8571` n `20`; unknown avg `-0.5174` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
