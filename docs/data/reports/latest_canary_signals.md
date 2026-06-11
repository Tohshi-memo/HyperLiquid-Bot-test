# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T11:07:27.086513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0447` n `12`; crypto_alt avg `0.1492` n `228`; crypto_major avg `0.1812` n `8`; equity avg `-0.1479` n `74`; fx avg `0.0138` n `6`; index avg `-0.1136` n `23`; metal avg `-0.046` n `18`; unknown avg `0.1236` n `556`
- 1h: commodity avg `-0.1761` n `12`; crypto_alt avg `-0.0821` n `228`; crypto_major avg `0.1761` n `8`; equity avg `-0.202` n `74`; fx avg `0.0023` n `6`; index avg `-0.1254` n `23`; metal avg `-0.0315` n `18`; unknown avg `-1.7114` n `556`
- 4h: commodity avg `-0.6088` n `12`; crypto_alt avg `0.6407` n `228`; crypto_major avg `0.7286` n `8`; equity avg `0.4811` n `74`; fx avg `-0.0731` n `6`; index avg `0.2252` n `23`; metal avg `-0.1533` n `18`; unknown avg `0.9219` n `548`
- 24h: commodity avg `-0.4519` n `12`; crypto_alt avg `2.3755` n `228`; crypto_major avg `2.188` n `8`; equity avg `1.1425` n `74`; fx avg `0.0197` n `6`; index avg `0.272` n `23`; metal avg `-0.379` n `18`; unknown avg `4.5601` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
