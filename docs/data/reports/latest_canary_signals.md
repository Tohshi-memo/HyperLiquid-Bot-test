# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T12:22:26.032650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1131` n `12`; crypto_alt avg `0.0099` n `230`; crypto_major avg `-0.0023` n `8`; equity avg `0.1106` n `94`; fx avg `-0.0038` n `6`; index avg `-0.0156` n `25`; metal avg `-0.1334` n `20`; unknown avg `-0.0125` n `768`
- 1h: commodity avg `0.3023` n `12`; crypto_alt avg `0.0272` n `230`; crypto_major avg `0.0133` n `8`; equity avg `-0.115` n `94`; fx avg `0.0369` n `6`; index avg `-0.066` n `25`; metal avg `-0.0795` n `20`; unknown avg `0.178` n `768`
- 4h: commodity avg `0.3238` n `12`; crypto_alt avg `0.2916` n `230`; crypto_major avg `0.2588` n `8`; equity avg `-0.425` n `94`; fx avg `0.0051` n `6`; index avg `-0.1137` n `25`; metal avg `-0.1571` n `20`; unknown avg `0.3433` n `762`
- 24h: commodity avg `0.2869` n `12`; crypto_alt avg `-0.8049` n `230`; crypto_major avg `-0.8417` n `8`; equity avg `-3.0564` n `93`; fx avg `0.0398` n `6`; index avg `-0.5405` n `25`; metal avg `-0.1499` n `20`; unknown avg `0.1736` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
