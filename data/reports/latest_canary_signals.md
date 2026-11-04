# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T14:07:29.053783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0606` n `13`; crypto_alt avg `-0.1957` n `239`; crypto_major avg `-0.064` n `8`; equity avg `-0.0603` n `158`; fx avg `-0.0046` n `6`; index avg `-0.0187` n `27`; metal avg `-0.0012` n `20`; unknown avg `-0.0491` n `1258`
- 1h: commodity avg `-0.2398` n `13`; crypto_alt avg `-0.2377` n `239`; crypto_major avg `-0.0581` n `8`; equity avg `0.1828` n `158`; fx avg `0.0006` n `6`; index avg `0.0218` n `27`; metal avg `0.014` n `20`; unknown avg `0.0008` n `1258`
- 4h: commodity avg `-0.4911` n `13`; crypto_alt avg `-0.864` n `239`; crypto_major avg `-0.5804` n `8`; equity avg `-1.7018` n `158`; fx avg `0.0125` n `6`; index avg `-0.0787` n `27`; metal avg `-0.0569` n `20`; unknown avg `0.8185` n `1254`
- 24h: commodity avg `-0.4284` n `13`; crypto_alt avg `0.6438` n `239`; crypto_major avg `0.2431` n `8`; equity avg `0.0393` n `158`; fx avg `0.179` n `6`; index avg `0.0424` n `27`; metal avg `0.6776` n `20`; unknown avg `-0.1569` n `1089`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2549`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
