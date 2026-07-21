# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T23:43:37.992915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0296` n `12`; crypto_alt avg `0.1746` n `230`; crypto_major avg `0.1832` n `8`; equity avg `-0.0092` n `98`; fx avg `0.0012` n `6`; index avg `0.0003` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.0325` n `771`
- 1h: commodity avg `0.0098` n `12`; crypto_alt avg `0.0336` n `230`; crypto_major avg `-0.0078` n `8`; equity avg `0.1568` n `98`; fx avg `0.0038` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0077` n `20`; unknown avg `-0.1244` n `771`
- 4h: commodity avg `0.0506` n `12`; crypto_alt avg `-0.0508` n `230`; crypto_major avg `-0.1931` n `8`; equity avg `0.6982` n `98`; fx avg `-0.0157` n `6`; index avg `0.0175` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.2513` n `771`
- 24h: commodity avg `0.4929` n `12`; crypto_alt avg `0.7537` n `230`; crypto_major avg `0.5835` n `8`; equity avg `4.3747` n `98`; fx avg `0.0616` n `6`; index avg `0.6053` n `25`; metal avg `0.769` n `20`; unknown avg `0.3856` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0889`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0501`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0498`, n `666`, weak_sample_signal
