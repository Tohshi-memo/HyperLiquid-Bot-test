# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T14:52:31.990342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `-0.4599` n `234`; crypto_major avg `-0.5216` n `8`; equity avg `-0.0621` n `141`; fx avg `-0.0102` n `6`; index avg `-0.0075` n `26`; metal avg `0.0299` n `20`; unknown avg `4.7252` n `960`
- 1h: commodity avg `0.0629` n `12`; crypto_alt avg `-0.2895` n `234`; crypto_major avg `-0.3417` n `8`; equity avg `-0.534` n `141`; fx avg `0.0358` n `6`; index avg `-0.0952` n `26`; metal avg `-0.0453` n `20`; unknown avg `15.4012` n `922`
- 4h: commodity avg `-0.0642` n `12`; crypto_alt avg `-0.4673` n `234`; crypto_major avg `-0.6363` n `8`; equity avg `-1.181` n `141`; fx avg `-0.0123` n `6`; index avg `-0.1103` n `26`; metal avg `-0.2666` n `20`; unknown avg `17.7528` n `916`
- 24h: commodity avg `-0.3717` n `12`; crypto_alt avg `2.7921` n `234`; crypto_major avg `1.7121` n `8`; equity avg `0.3952` n `141`; fx avg `-0.2212` n `6`; index avg `0.1385` n `26`; metal avg `0.0962` n `20`; unknown avg `14.3617` n `801`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
