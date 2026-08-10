# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T18:52:36.865049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0465` n `12`; crypto_alt avg `0.0557` n `230`; crypto_major avg `0.0084` n `8`; equity avg `0.102` n `113`; fx avg `0.0149` n `6`; index avg `0.0188` n `25`; metal avg `0.0177` n `20`; unknown avg `0.1243` n `785`
- 1h: commodity avg `0.0483` n `12`; crypto_alt avg `-0.1216` n `230`; crypto_major avg `-0.1173` n `8`; equity avg `-0.0678` n `113`; fx avg `0.0113` n `6`; index avg `0.0135` n `25`; metal avg `0.1187` n `20`; unknown avg `-0.1692` n `785`
- 4h: commodity avg `0.2277` n `12`; crypto_alt avg `-0.3849` n `230`; crypto_major avg `-0.5549` n `8`; equity avg `-0.2454` n `113`; fx avg `0.0142` n `6`; index avg `-0.0444` n `25`; metal avg `0.2288` n `20`; unknown avg `-0.1443` n `784`
- 24h: commodity avg `1.197` n `12`; crypto_alt avg `-0.8367` n `230`; crypto_major avg `-1.3628` n `8`; equity avg `-1.358` n `113`; fx avg `0.2646` n `6`; index avg `-0.0789` n `25`; metal avg `0.1256` n `20`; unknown avg `103.5131` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
