# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T07:37:28.519249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.029` n `12`; crypto_alt avg `0.1038` n `228`; crypto_major avg `0.1116` n `8`; equity avg `0.0247` n `88`; fx avg `0.0116` n `6`; index avg `0.0021` n `23`; metal avg `0.0091` n `20`; unknown avg `0.0235` n `764`
- 1h: commodity avg `0.0578` n `12`; crypto_alt avg `0.3962` n `228`; crypto_major avg `0.4296` n `8`; equity avg `0.0907` n `88`; fx avg `0.0184` n `6`; index avg `0.0056` n `23`; metal avg `-0.0097` n `20`; unknown avg `-0.9774` n `764`
- 4h: commodity avg `0.0724` n `12`; crypto_alt avg `0.0379` n `228`; crypto_major avg `-0.0201` n `8`; equity avg `0.0373` n `88`; fx avg `0.0195` n `6`; index avg `-0.0034` n `23`; metal avg `-0.0343` n `20`; unknown avg `-1.3857` n `732`
- 24h: commodity avg `0.3297` n `12`; crypto_alt avg `-0.45` n `228`; crypto_major avg `-1.1074` n `8`; equity avg `-0.0289` n `88`; fx avg `-0.0319` n `6`; index avg `-0.1287` n `23`; metal avg `-0.0372` n `20`; unknown avg `14.5634` n `698`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2181`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
