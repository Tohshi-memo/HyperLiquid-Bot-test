# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T19:22:25.633282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `0.1056` n `230`; crypto_major avg `0.2753` n `8`; equity avg `0.0439` n `121`; fx avg `0.0051` n `6`; index avg `-0.004` n `25`; metal avg `0.0105` n `20`; unknown avg `-0.0768` n `793`
- 1h: commodity avg `-0.0838` n `12`; crypto_alt avg `-1.3073` n `230`; crypto_major avg `-0.6586` n `8`; equity avg `0.0125` n `121`; fx avg `0.002` n `6`; index avg `0.0052` n `25`; metal avg `-0.0188` n `20`; unknown avg `1.0934` n `793`
- 4h: commodity avg `-0.0692` n `12`; crypto_alt avg `-1.2684` n `230`; crypto_major avg `-0.9655` n `8`; equity avg `-0.0011` n `121`; fx avg `0.0301` n `6`; index avg `0.0125` n `25`; metal avg `0.0975` n `20`; unknown avg `1.0598` n `793`
- 24h: commodity avg `0.0921` n `12`; crypto_alt avg `6.4534` n `230`; crypto_major avg `4.769` n `8`; equity avg `1.1927` n `121`; fx avg `-0.0913` n `6`; index avg `0.1194` n `25`; metal avg `0.5723` n `20`; unknown avg `2.1952` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
