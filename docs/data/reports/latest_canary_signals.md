# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T23:22:17.620323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1682` n `12`; crypto_alt avg `-0.092` n `228`; crypto_major avg `-0.0756` n `8`; equity avg `-0.0463` n `66`; fx avg `-0.0066` n `6`; index avg `-0.0017` n `23`; metal avg `-0.0835` n `18`; unknown avg `-0.0574` n `384`
- 1h: commodity avg `-0.0707` n `12`; crypto_alt avg `0.1179` n `228`; crypto_major avg `0.2738` n `8`; equity avg `0.2437` n `66`; fx avg `-0.007` n `6`; index avg `0.0846` n `23`; metal avg `0.1195` n `18`; unknown avg `0.051` n `384`
- 4h: commodity avg `-0.031` n `12`; crypto_alt avg `-0.352` n `228`; crypto_major avg `0.1404` n `8`; equity avg `-0.1878` n `66`; fx avg `-0.0678` n `6`; index avg `-0.2275` n `23`; metal avg `-0.3514` n `18`; unknown avg `-0.2405` n `384`
- 24h: commodity avg `-2.5552` n `12`; crypto_alt avg `2.6288` n `228`; crypto_major avg `2.0636` n `8`; equity avg `1.4111` n `66`; fx avg `-0.0766` n `6`; index avg `0.9621` n `23`; metal avg `1.1298` n `18`; unknown avg `1.01` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
