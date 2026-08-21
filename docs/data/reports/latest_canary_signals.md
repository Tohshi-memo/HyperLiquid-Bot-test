# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T18:22:35.052055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `0.0138` n `230`; crypto_major avg `0.0579` n `8`; equity avg `0.0646` n `121`; fx avg `-0.0058` n `6`; index avg `0.003` n `25`; metal avg `0.0062` n `20`; unknown avg `0.0922` n `793`
- 1h: commodity avg `0.049` n `12`; crypto_alt avg `0.6957` n `230`; crypto_major avg `0.425` n `8`; equity avg `0.1467` n `121`; fx avg `0.0068` n `6`; index avg `-0.0047` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.038` n `793`
- 4h: commodity avg `0.1208` n `12`; crypto_alt avg `0.7565` n `230`; crypto_major avg `0.5249` n `8`; equity avg `0.3597` n `121`; fx avg `0.022` n `6`; index avg `0.0498` n `25`; metal avg `-0.0122` n `20`; unknown avg `0.1185` n `793`
- 24h: commodity avg `0.3357` n `12`; crypto_alt avg `7.867` n `230`; crypto_major avg `4.8275` n `8`; equity avg `1.4749` n `121`; fx avg `-0.0985` n `6`; index avg `0.1563` n `25`; metal avg `0.6637` n `20`; unknown avg `1.214` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
