# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T17:07:25.384345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0678` n `12`; crypto_alt avg `-0.0532` n `228`; crypto_major avg `-0.2388` n `8`; equity avg `-0.041` n `74`; fx avg `-0.0005` n `6`; index avg `-0.0097` n `23`; metal avg `0.0485` n `18`; unknown avg `3.9427` n `424`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `0.1968` n `228`; crypto_major avg `0.0232` n `8`; equity avg `0.1028` n `74`; fx avg `-0.0107` n `6`; index avg `0.1478` n `23`; metal avg `0.0623` n `18`; unknown avg `4.1121` n `424`
- 4h: commodity avg `-0.0244` n `12`; crypto_alt avg `1.0225` n `228`; crypto_major avg `0.1729` n `8`; equity avg `1.055` n `74`; fx avg `-0.0469` n `6`; index avg `0.7208` n `23`; metal avg `-0.4593` n `18`; unknown avg `4.0572` n `424`
- 24h: commodity avg `-0.7766` n `12`; crypto_alt avg `-4.1962` n `228`; crypto_major avg `-3.1178` n `8`; equity avg `-0.8247` n `73`; fx avg `0.0825` n `6`; index avg `-0.1317` n `23`; metal avg `0.5539` n `18`; unknown avg `3.2856` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
