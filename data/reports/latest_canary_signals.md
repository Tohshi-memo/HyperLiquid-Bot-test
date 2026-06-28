# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T14:55:54.101563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0472` n `12`; crypto_alt avg `-0.0949` n `228`; crypto_major avg `-0.1531` n `8`; equity avg `0.002` n `88`; fx avg `0.0196` n `6`; index avg `-0.0004` n `23`; metal avg `-0.0224` n `20`; unknown avg `-0.0194` n `764`
- 1h: commodity avg `0.0561` n `12`; crypto_alt avg `0.5732` n `228`; crypto_major avg `-0.0041` n `8`; equity avg `0.0027` n `88`; fx avg `0.0104` n `6`; index avg `0.0086` n `23`; metal avg `-0.0256` n `20`; unknown avg `2.6641` n `764`
- 4h: commodity avg `0.1359` n `12`; crypto_alt avg `0.6785` n `228`; crypto_major avg `0.2109` n `8`; equity avg `0.0967` n `88`; fx avg `0.011` n `6`; index avg `0.0295` n `23`; metal avg `-0.0358` n `20`; unknown avg `1.7964` n `764`
- 24h: commodity avg `0.2297` n `12`; crypto_alt avg `-0.1447` n `228`; crypto_major avg `-1.3077` n `8`; equity avg `0.0397` n `88`; fx avg `0.0087` n `6`; index avg `-0.0408` n `23`; metal avg `-0.0736` n `20`; unknown avg `16.3003` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
