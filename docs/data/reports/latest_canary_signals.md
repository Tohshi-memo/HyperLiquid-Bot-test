# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T20:21:41.251791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0878` n `12`; crypto_alt avg `0.3262` n `228`; crypto_major avg `0.2472` n `8`; equity avg `0.0802` n `88`; fx avg `-0.0137` n `6`; index avg `0.0082` n `23`; metal avg `0.0256` n `20`; unknown avg `-0.1581` n `764`
- 1h: commodity avg `-0.0228` n `12`; crypto_alt avg `0.0476` n `228`; crypto_major avg `0.1761` n `8`; equity avg `0.1286` n `88`; fx avg `0.0142` n `6`; index avg `0.0057` n `23`; metal avg `0.0048` n `20`; unknown avg `2.847` n `764`
- 4h: commodity avg `-0.1174` n `12`; crypto_alt avg `-0.7434` n `228`; crypto_major avg `-0.6107` n `8`; equity avg `0.0395` n `88`; fx avg `-0.0395` n `6`; index avg `-0.0047` n `23`; metal avg `0.019` n `20`; unknown avg `3.1775` n `764`
- 24h: commodity avg `0.2551` n `12`; crypto_alt avg `-0.4205` n `228`; crypto_major avg `-0.8683` n `8`; equity avg `0.203` n `88`; fx avg `-0.0482` n `6`; index avg `-0.0503` n `23`; metal avg `0.0066` n `20`; unknown avg `15.7228` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
