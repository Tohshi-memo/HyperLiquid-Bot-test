# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T21:07:28.940018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.4016` n `234`; crypto_major avg `-0.2934` n `8`; equity avg `-0.0079` n `140`; fx avg `0.0039` n `6`; index avg `0.0087` n `26`; metal avg `-0.0053` n `20`; unknown avg `19.422` n `939`
- 1h: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.3515` n `234`; crypto_major avg `-0.4414` n `8`; equity avg `0.0228` n `140`; fx avg `0.0126` n `6`; index avg `0.0268` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.4926` n `905`
- 4h: commodity avg `0.0278` n `12`; crypto_alt avg `-0.0297` n `234`; crypto_major avg `-0.3203` n `8`; equity avg `0.0476` n `140`; fx avg `0.0009` n `6`; index avg `0.0167` n `26`; metal avg `-0.026` n `20`; unknown avg `1.3153` n `879`
- 24h: commodity avg `0.347` n `12`; crypto_alt avg `0.6135` n `234`; crypto_major avg `-0.4255` n `8`; equity avg `-0.0906` n `140`; fx avg `0.0147` n `6`; index avg `-0.046` n `26`; metal avg `-0.0409` n `20`; unknown avg `2.7195` n `791`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
