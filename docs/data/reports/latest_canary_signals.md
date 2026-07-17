# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T22:37:28.652502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `-0.0176` n `230`; crypto_major avg `-0.0188` n `8`; equity avg `0.0452` n `96`; fx avg `0.003` n `6`; index avg `-0.0016` n `25`; metal avg `0.0133` n `20`; unknown avg `0.0112` n `769`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `-0.1696` n `230`; crypto_major avg `-0.2071` n `8`; equity avg `-0.0071` n `96`; fx avg `-0.0059` n `6`; index avg `-0.017` n `25`; metal avg `0.0343` n `20`; unknown avg `0.1483` n `769`
- 4h: commodity avg `0.1092` n `12`; crypto_alt avg `-0.4293` n `230`; crypto_major avg `-0.0913` n `8`; equity avg `-0.5771` n `96`; fx avg `-0.0587` n `6`; index avg `-0.1195` n `25`; metal avg `-0.0047` n `20`; unknown avg `-0.1493` n `769`
- 24h: commodity avg `0.7031` n `12`; crypto_alt avg `-1.0462` n `230`; crypto_major avg `-1.0272` n `8`; equity avg `-1.2474` n `94`; fx avg `0.0517` n `6`; index avg `-0.2862` n `25`; metal avg `0.0512` n `20`; unknown avg `-0.0042` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
