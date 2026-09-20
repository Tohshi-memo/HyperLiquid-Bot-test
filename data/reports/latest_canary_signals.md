# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T23:37:26.118195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `0.1797` n `234`; crypto_major avg `0.1447` n `8`; equity avg `0.0224` n `140`; fx avg `-0.0147` n `6`; index avg `0.003` n `26`; metal avg `0.0091` n `20`; unknown avg `0.1669` n `945`
- 1h: commodity avg `-0.0566` n `12`; crypto_alt avg `-0.1885` n `234`; crypto_major avg `0.164` n `8`; equity avg `0.1849` n `140`; fx avg `-0.009` n `6`; index avg `0.0273` n `26`; metal avg `-0.0223` n `20`; unknown avg `23.3766` n `941`
- 4h: commodity avg `-0.3501` n `12`; crypto_alt avg `0.5718` n `234`; crypto_major avg `0.253` n `8`; equity avg `0.5189` n `140`; fx avg `0.0393` n `6`; index avg `0.1128` n `26`; metal avg `0.0536` n `20`; unknown avg `2.4145` n `853`
- 24h: commodity avg `-0.0386` n `12`; crypto_alt avg `1.0659` n `234`; crypto_major avg `0.4082` n `8`; equity avg `0.4299` n `140`; fx avg `0.0513` n `6`; index avg `0.0693` n `26`; metal avg `0.0238` n `20`; unknown avg `4.1228` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
