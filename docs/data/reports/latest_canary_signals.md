# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T21:22:27.673359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0273` n `12`; crypto_alt avg `0.0257` n `230`; crypto_major avg `-0.0187` n `8`; equity avg `0.0659` n `113`; fx avg `-0.0099` n `6`; index avg `0.0142` n `25`; metal avg `-0.0189` n `20`; unknown avg `0.1111` n `786`
- 1h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.0074` n `230`; crypto_major avg `0.0881` n `8`; equity avg `0.1436` n `113`; fx avg `-0.0161` n `6`; index avg `0.0078` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.0052` n `786`
- 4h: commodity avg `0.0006` n `12`; crypto_alt avg `-0.2466` n `230`; crypto_major avg `-0.0354` n `8`; equity avg `-0.0393` n `113`; fx avg `-0.026` n `6`; index avg `0.0171` n `25`; metal avg `-0.0518` n `20`; unknown avg `0.628` n `786`
- 24h: commodity avg `0.0718` n `12`; crypto_alt avg `-0.7723` n `230`; crypto_major avg `-0.0606` n `8`; equity avg `2.8792` n `113`; fx avg `0.017` n `6`; index avg `0.3955` n `25`; metal avg `0.1661` n `20`; unknown avg `0.0754` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2025`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
