# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T13:07:30.026944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.032` n `12`; crypto_alt avg `0.2689` n `234`; crypto_major avg `0.3291` n `8`; equity avg `-0.0089` n `140`; fx avg `-0.0017` n `6`; index avg `-0.0115` n `26`; metal avg `0.0176` n `20`; unknown avg `-0.0682` n `942`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.6456` n `234`; crypto_major avg `0.2694` n `8`; equity avg `-0.0498` n `140`; fx avg `-0.0152` n `6`; index avg `-0.0312` n `26`; metal avg `0.087` n `20`; unknown avg `1.1479` n `940`
- 4h: commodity avg `-0.2392` n `12`; crypto_alt avg `1.4824` n `234`; crypto_major avg `1.1572` n `8`; equity avg `0.0787` n `140`; fx avg `0.0314` n `6`; index avg `0.0194` n `26`; metal avg `0.1954` n `20`; unknown avg `0.1584` n `910`
- 24h: commodity avg `-0.8631` n `12`; crypto_alt avg `7.3738` n `234`; crypto_major avg `6.1487` n `8`; equity avg `2.0697` n `140`; fx avg `-0.0667` n `6`; index avg `0.3659` n `26`; metal avg `0.2641` n `20`; unknown avg `3.8525` n `733`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
