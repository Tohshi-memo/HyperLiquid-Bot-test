# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T08:07:38.791340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `12`; crypto_alt avg `0.1284` n `228`; crypto_major avg `0.1547` n `8`; equity avg `0.0112` n `88`; fx avg `0.001` n `6`; index avg `-0.0239` n `25`; metal avg `0.0028` n `20`; unknown avg `0.4892` n `763`
- 1h: commodity avg `0.1182` n `12`; crypto_alt avg `0.3482` n `228`; crypto_major avg `0.2393` n `8`; equity avg `0.0827` n `88`; fx avg `-0.0183` n `6`; index avg `0.0003` n `25`; metal avg `-0.0659` n `20`; unknown avg `1.1253` n `763`
- 4h: commodity avg `0.0081` n `12`; crypto_alt avg `-0.2314` n `228`; crypto_major avg `-0.5281` n `8`; equity avg `-1.1256` n `88`; fx avg `-0.0301` n `6`; index avg `-0.2495` n `25`; metal avg `-0.2067` n `20`; unknown avg `1.1364` n `741`
- 24h: commodity avg `-0.5108` n `12`; crypto_alt avg `2.2808` n `228`; crypto_major avg `1.6048` n `8`; equity avg `-2.2225` n `88`; fx avg `-0.0749` n `6`; index avg `-0.5738` n `25`; metal avg `1.1031` n `20`; unknown avg `15.9429` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
