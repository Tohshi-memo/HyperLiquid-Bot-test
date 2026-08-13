# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T11:07:29.791342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.0665` n `230`; crypto_major avg `-0.0355` n `8`; equity avg `0.0803` n `113`; fx avg `-0.0001` n `6`; index avg `0.0067` n `25`; metal avg `-0.015` n `20`; unknown avg `-0.0382` n `787`
- 1h: commodity avg `-0.1041` n `12`; crypto_alt avg `-0.0669` n `230`; crypto_major avg `-0.1751` n `8`; equity avg `0.0125` n `113`; fx avg `-0.0052` n `6`; index avg `0.0094` n `25`; metal avg `0.0876` n `20`; unknown avg `-0.0258` n `787`
- 4h: commodity avg `-0.2799` n `12`; crypto_alt avg `-0.1149` n `230`; crypto_major avg `-0.5111` n `8`; equity avg `0.0642` n `113`; fx avg `0.007` n `6`; index avg `0.0121` n `25`; metal avg `0.0681` n `20`; unknown avg `-0.0336` n `787`
- 24h: commodity avg `-0.36` n `12`; crypto_alt avg `-0.6642` n `230`; crypto_major avg `-0.535` n `8`; equity avg `1.3841` n `113`; fx avg `0.0463` n `6`; index avg `0.163` n `25`; metal avg `-0.5067` n `20`; unknown avg `0.0971` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2249`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
