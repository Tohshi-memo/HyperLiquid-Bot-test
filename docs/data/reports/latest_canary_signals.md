# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T10:07:30.051250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `12`; crypto_alt avg `-0.141` n `233`; crypto_major avg `-0.044` n `8`; equity avg `-0.2681` n `134`; fx avg `0.0056` n `6`; index avg `-0.0447` n `26`; metal avg `-0.0125` n `20`; unknown avg `0.3781` n `796`
- 1h: commodity avg `0.0071` n `12`; crypto_alt avg `-0.923` n `233`; crypto_major avg `-0.7818` n `8`; equity avg `-0.7789` n `134`; fx avg `-0.0124` n `6`; index avg `-0.1397` n `26`; metal avg `-0.0774` n `20`; unknown avg `0.865` n `796`
- 4h: commodity avg `0.2228` n `12`; crypto_alt avg `0.0653` n `233`; crypto_major avg `-0.1468` n `8`; equity avg `-0.6325` n `134`; fx avg `0.0302` n `6`; index avg `-0.164` n `26`; metal avg `-0.0785` n `20`; unknown avg `0.75` n `790`
- 24h: commodity avg `-0.0364` n `12`; crypto_alt avg `-0.7285` n `232`; crypto_major avg `0.3776` n `8`; equity avg `0.3092` n `134`; fx avg `-0.0817` n `6`; index avg `-0.147` n `26`; metal avg `-0.1226` n `20`; unknown avg `0.9854` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
