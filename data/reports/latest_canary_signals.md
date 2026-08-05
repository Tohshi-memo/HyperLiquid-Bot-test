# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T04:37:30.156920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.1025` n `230`; crypto_major avg `0.1082` n `8`; equity avg `0.1377` n `108`; fx avg `0.0171` n `6`; index avg `0.0352` n `25`; metal avg `-0.026` n `20`; unknown avg `-0.1008` n `781`
- 1h: commodity avg `0.1094` n `12`; crypto_alt avg `0.2216` n `230`; crypto_major avg `0.107` n `8`; equity avg `0.1245` n `108`; fx avg `0.005` n `6`; index avg `0.0179` n `25`; metal avg `0.0257` n `20`; unknown avg `0.0111` n `781`
- 4h: commodity avg `-0.0439` n `12`; crypto_alt avg `0.4904` n `230`; crypto_major avg `0.2122` n `8`; equity avg `0.3086` n `108`; fx avg `-0.043` n `6`; index avg `-0.0245` n `25`; metal avg `0.3407` n `20`; unknown avg `-0.2096` n `781`
- 24h: commodity avg `-1.4459` n `12`; crypto_alt avg `0.3599` n `230`; crypto_major avg `0.4101` n `8`; equity avg `4.1283` n `108`; fx avg `-0.0112` n `6`; index avg `0.8507` n `25`; metal avg `1.0137` n `20`; unknown avg `0.3924` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
