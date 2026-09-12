# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T11:13:52.724283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `0.058` n `233`; crypto_major avg `0.0326` n `8`; equity avg `0.0243` n `136`; fx avg `-0.0046` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.0177` n `836`
- 1h: commodity avg `-0.0214` n `12`; crypto_alt avg `0.07` n `233`; crypto_major avg `-0.0023` n `8`; equity avg `0.0049` n `136`; fx avg `-0.0052` n `6`; index avg `-0.001` n `26`; metal avg `0.0026` n `20`; unknown avg `0.5148` n `836`
- 4h: commodity avg `0.0587` n `12`; crypto_alt avg `0.4097` n `233`; crypto_major avg `0.4921` n `8`; equity avg `0.0508` n `136`; fx avg `-0.0068` n `6`; index avg `-0.0011` n `26`; metal avg `0.002` n `20`; unknown avg `0.8147` n `830`
- 24h: commodity avg `-0.0141` n `12`; crypto_alt avg `3.3287` n `233`; crypto_major avg `2.3121` n `8`; equity avg `0.2982` n `136`; fx avg `-0.0257` n `6`; index avg `0.1329` n `26`; metal avg `0.0212` n `20`; unknown avg `1.1387` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
