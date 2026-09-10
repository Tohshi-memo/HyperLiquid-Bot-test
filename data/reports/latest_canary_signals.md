# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T03:07:23.667931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `0.1587` n `233`; crypto_major avg `0.1202` n `8`; equity avg `0.0176` n `134`; fx avg `0.018` n `6`; index avg `0.0102` n `26`; metal avg `-0.0363` n `20`; unknown avg `120.1558` n `795`
- 1h: commodity avg `-0.0447` n `12`; crypto_alt avg `0.6801` n `233`; crypto_major avg `0.5578` n `8`; equity avg `0.1902` n `134`; fx avg `0.0207` n `6`; index avg `0.041` n `26`; metal avg `-0.0127` n `20`; unknown avg `26.0592` n `795`
- 4h: commodity avg `-0.2141` n `12`; crypto_alt avg `0.1788` n `233`; crypto_major avg `0.5387` n `8`; equity avg `-0.2072` n `134`; fx avg `0.0124` n `6`; index avg `0.0127` n `26`; metal avg `0.0039` n `20`; unknown avg `120.8452` n `789`
- 24h: commodity avg `-0.0878` n `12`; crypto_alt avg `-2.5865` n `233`; crypto_major avg `-1.6188` n `8`; equity avg `-1.2114` n `134`; fx avg `0.0176` n `6`; index avg `-0.2012` n `26`; metal avg `0.411` n `20`; unknown avg `1.6659` n `667`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
