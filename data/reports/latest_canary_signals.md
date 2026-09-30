# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T20:37:34.691472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0687` n `12`; crypto_alt avg `-0.1403` n `234`; crypto_major avg `0.0287` n `8`; equity avg `0.0585` n `142`; fx avg `-0.0001` n `6`; index avg `0.0185` n `26`; metal avg `0.0151` n `20`; unknown avg `0.2574` n `935`
- 1h: commodity avg `-0.0647` n `12`; crypto_alt avg `0.0939` n `234`; crypto_major avg `0.0958` n `8`; equity avg `0.0242` n `142`; fx avg `0.0179` n `6`; index avg `-0.0206` n `26`; metal avg `0.0055` n `20`; unknown avg `0.0923` n `889`
- 4h: commodity avg `-0.1787` n `12`; crypto_alt avg `-1.0151` n `234`; crypto_major avg `-0.343` n `8`; equity avg `-0.0431` n `142`; fx avg `0.0057` n `6`; index avg `-0.0771` n `26`; metal avg `0.0416` n `20`; unknown avg `2.918` n `889`
- 24h: commodity avg `0.3408` n `12`; crypto_alt avg `0.075` n `234`; crypto_major avg `0.6974` n `8`; equity avg `-0.1898` n `142`; fx avg `0.0804` n `6`; index avg `-0.0247` n `26`; metal avg `-0.2162` n `20`; unknown avg `790.0657` n `786`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
