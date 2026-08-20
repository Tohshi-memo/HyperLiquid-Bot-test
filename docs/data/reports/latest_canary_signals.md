# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T13:07:25.789623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.1819` n `230`; crypto_major avg `0.3734` n `8`; equity avg `0.1298` n `121`; fx avg `-0.0033` n `6`; index avg `0.0268` n `25`; metal avg `0.0433` n `20`; unknown avg `0.1167` n `792`
- 1h: commodity avg `-0.0943` n `12`; crypto_alt avg `0.286` n `230`; crypto_major avg `0.6048` n `8`; equity avg `0.1701` n `121`; fx avg `-0.0113` n `6`; index avg `0.0506` n `25`; metal avg `0.2535` n `20`; unknown avg `0.1216` n `792`
- 4h: commodity avg `0.0322` n `12`; crypto_alt avg `0.4868` n `230`; crypto_major avg `0.3251` n `8`; equity avg `-0.8607` n `121`; fx avg `0.007` n `6`; index avg `-0.1267` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.5056` n `792`
- 24h: commodity avg `0.1901` n `12`; crypto_alt avg `7.4853` n `230`; crypto_major avg `12.2396` n `8`; equity avg `-1.4784` n `120`; fx avg `0.2231` n `6`; index avg `-0.22` n `25`; metal avg `0.4669` n `20`; unknown avg `2.7814` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
