# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T19:37:28.706654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0587` n `12`; crypto_alt avg `0.0039` n `234`; crypto_major avg `0.0161` n `8`; equity avg `-0.0907` n `141`; fx avg `0.0002` n `6`; index avg `-0.0036` n `26`; metal avg `0.0126` n `20`; unknown avg `117.463` n `960`
- 1h: commodity avg `0.027` n `12`; crypto_alt avg `0.1568` n `234`; crypto_major avg `0.0501` n `8`; equity avg `-0.0835` n `141`; fx avg `0.0056` n `6`; index avg `0.0012` n `26`; metal avg `0.0186` n `20`; unknown avg `14.8489` n `958`
- 4h: commodity avg `-0.2813` n `12`; crypto_alt avg `1.1126` n `234`; crypto_major avg `0.5242` n `8`; equity avg `0.1146` n `141`; fx avg `-0.0211` n `6`; index avg `0.1003` n `26`; metal avg `0.1006` n `20`; unknown avg `7.6398` n `930`
- 24h: commodity avg `-0.9519` n `12`; crypto_alt avg `1.9238` n `234`; crypto_major avg `0.5975` n `8`; equity avg `0.0852` n `141`; fx avg `-0.2517` n `6`; index avg `0.2105` n `26`; metal avg `0.176` n `20`; unknown avg `1591.1158` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
