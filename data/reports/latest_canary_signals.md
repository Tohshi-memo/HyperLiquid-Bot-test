# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T17:38:21.540538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0313` n `12`; crypto_alt avg `0.0952` n `230`; crypto_major avg `0.0042` n `8`; equity avg `0.107` n `94`; fx avg `0.0186` n `6`; index avg `0.0536` n `25`; metal avg `0.1847` n `20`; unknown avg `-0.0642` n `768`
- 1h: commodity avg `-0.0341` n `12`; crypto_alt avg `0.4942` n `230`; crypto_major avg `0.5481` n `8`; equity avg `1.1913` n `94`; fx avg `0.0573` n `6`; index avg `0.2019` n `25`; metal avg `0.3197` n `20`; unknown avg `-0.0252` n `768`
- 4h: commodity avg `0.0087` n `12`; crypto_alt avg `-1.0102` n `230`; crypto_major avg `-1.0101` n `8`; equity avg `-1.6963` n `93`; fx avg `0.1368` n `6`; index avg `-0.2978` n `25`; metal avg `-0.1476` n `20`; unknown avg `0.1896` n `768`
- 24h: commodity avg `0.0898` n `12`; crypto_alt avg `0.4035` n `230`; crypto_major avg `1.2186` n `8`; equity avg `-0.5511` n `93`; fx avg `0.2159` n `6`; index avg `-0.2429` n `25`; metal avg `-0.0719` n `20`; unknown avg `0.279` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
