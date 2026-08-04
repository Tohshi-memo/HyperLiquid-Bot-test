# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T17:07:55.609190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6799` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0455` n `12`; crypto_alt avg `0.217` n `230`; crypto_major avg `0.3453` n `8`; equity avg `0.1135` n `107`; fx avg `0.0018` n `6`; index avg `0.0489` n `25`; metal avg `0.0322` n `20`; unknown avg `0.0129` n `782`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `0.1553` n `230`; crypto_major avg `0.2484` n `8`; equity avg `0.1637` n `107`; fx avg `0.0082` n `6`; index avg `0.0759` n `25`; metal avg `0.1026` n `20`; unknown avg `0.0036` n `782`
- 4h: commodity avg `-0.4623` n `12`; crypto_alt avg `0.1091` n `230`; crypto_major avg `0.1147` n `8`; equity avg `1.7946` n `107`; fx avg `0.0277` n `6`; index avg `0.4366` n `25`; metal avg `0.3965` n `20`; unknown avg `-0.2462` n `781`
- 24h: commodity avg `-1.0986` n `12`; crypto_alt avg `-0.0734` n `230`; crypto_major avg `0.4401` n `8`; equity avg `4.385` n `107`; fx avg `0.0874` n `6`; index avg `0.8626` n `25`; metal avg `1.251` n `20`; unknown avg `0.5536` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
