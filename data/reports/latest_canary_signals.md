# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T21:22:32.624734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.008` n `234`; crypto_major avg `0.0512` n `8`; equity avg `0.0214` n `140`; fx avg `-0.0036` n `6`; index avg `0.0067` n `26`; metal avg `-0.0052` n `20`; unknown avg `-0.2788` n `919`
- 1h: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.2289` n `234`; crypto_major avg `-0.1972` n `8`; equity avg `0.0218` n `140`; fx avg `-0.0133` n `6`; index avg `0.0075` n `26`; metal avg `-0.0002` n `20`; unknown avg `63.7245` n `889`
- 4h: commodity avg `-0.2049` n `12`; crypto_alt avg `-0.1934` n `234`; crypto_major avg `-0.201` n `8`; equity avg `0.0255` n `140`; fx avg `-0.0214` n `6`; index avg `-0.0187` n `26`; metal avg `-0.1652` n `20`; unknown avg `2.682` n `865`
- 24h: commodity avg `-0.1984` n `12`; crypto_alt avg `3.7309` n `234`; crypto_major avg `1.8968` n `8`; equity avg `2.4128` n `138`; fx avg `-0.0202` n `6`; index avg `0.4474` n `26`; metal avg `0.5555` n `20`; unknown avg `4.3016` n `771`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
