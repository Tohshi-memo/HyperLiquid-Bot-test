# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T21:37:32.658401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.0508` n `230`; crypto_major avg `-0.017` n `8`; equity avg `0.0302` n `114`; fx avg `-0.0047` n `6`; index avg `0.0004` n `25`; metal avg `0.0074` n `20`; unknown avg `-0.0015` n `792`
- 1h: commodity avg `-0.0007` n `12`; crypto_alt avg `0.0932` n `230`; crypto_major avg `0.0316` n `8`; equity avg `0.0969` n `114`; fx avg `-0.0167` n `6`; index avg `0.0103` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0082` n `792`
- 4h: commodity avg `0.1216` n `12`; crypto_alt avg `0.0298` n `230`; crypto_major avg `0.0553` n `8`; equity avg `-0.2321` n `114`; fx avg `-0.0169` n `6`; index avg `-0.0527` n `25`; metal avg `-0.0197` n `20`; unknown avg `-0.1157` n `792`
- 24h: commodity avg `0.4055` n `12`; crypto_alt avg `0.4003` n `230`; crypto_major avg `1.0452` n `8`; equity avg `1.0758` n `114`; fx avg `0.005` n `6`; index avg `0.067` n `25`; metal avg `0.2212` n `20`; unknown avg `0.3139` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
