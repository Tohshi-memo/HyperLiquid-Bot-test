# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T14:07:34.493959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0921` n `12`; crypto_alt avg `0.1981` n `230`; crypto_major avg `0.3699` n `8`; equity avg `0.5532` n `93`; fx avg `-0.0041` n `6`; index avg `0.0954` n `25`; metal avg `0.0646` n `20`; unknown avg `-0.0407` n `768`
- 1h: commodity avg `-0.0166` n `12`; crypto_alt avg `-0.3353` n `230`; crypto_major avg `-0.2084` n `8`; equity avg `-0.3865` n `93`; fx avg `0.0319` n `6`; index avg `-0.1284` n `25`; metal avg `-0.0439` n `20`; unknown avg `-0.0634` n `768`
- 4h: commodity avg `-0.2249` n `12`; crypto_alt avg `0.8246` n `230`; crypto_major avg `1.0755` n `8`; equity avg `-0.2656` n `93`; fx avg `0.043` n `6`; index avg `-0.0979` n `25`; metal avg `0.2543` n `20`; unknown avg `0.168` n `767`
- 24h: commodity avg `0.0218` n `12`; crypto_alt avg `1.2477` n `230`; crypto_major avg `2.3689` n `8`; equity avg `1.0667` n `92`; fx avg `0.0678` n `6`; index avg `0.1064` n `25`; metal avg `-0.0199` n `20`; unknown avg `0.2245` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
