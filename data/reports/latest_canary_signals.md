# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T21:26:21.435375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `0.0482` n `232`; crypto_major avg `0.0519` n `8`; equity avg `0.0178` n `133`; fx avg `0.0032` n `6`; index avg `0.0037` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.0489` n `786`
- 1h: commodity avg `0.0359` n `12`; crypto_alt avg `0.207` n `232`; crypto_major avg `0.0371` n `8`; equity avg `-0.0104` n `133`; fx avg `0.0009` n `6`; index avg `-0.0055` n `26`; metal avg `0.0108` n `20`; unknown avg `0.0235` n `774`
- 4h: commodity avg `-0.1244` n `12`; crypto_alt avg `0.4566` n `232`; crypto_major avg `0.5119` n `8`; equity avg `0.1213` n `133`; fx avg `0.0099` n `6`; index avg `0.0281` n `26`; metal avg `-0.087` n `20`; unknown avg `-0.1844` n `772`
- 24h: commodity avg `-0.0317` n `12`; crypto_alt avg `4.5254` n `232`; crypto_major avg `5.4255` n `8`; equity avg `1.3365` n `133`; fx avg `-0.2109` n `6`; index avg `0.1822` n `26`; metal avg `0.7685` n `20`; unknown avg `29.3451` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
