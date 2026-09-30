# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T17:22:31.859783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0297` n `12`; crypto_alt avg `-0.2892` n `234`; crypto_major avg `-0.3353` n `8`; equity avg `-0.2064` n `142`; fx avg `-0.0093` n `6`; index avg `-0.0499` n `26`; metal avg `-0.0342` n `20`; unknown avg `0.4838` n `969`
- 1h: commodity avg `-0.0967` n `12`; crypto_alt avg `-0.3082` n `234`; crypto_major avg `0.0301` n `8`; equity avg `-0.2069` n `142`; fx avg `-0.0032` n `6`; index avg `-0.0745` n `26`; metal avg `-0.0403` n `20`; unknown avg `6.3781` n `967`
- 4h: commodity avg `-0.0453` n `12`; crypto_alt avg `-1.1751` n `234`; crypto_major avg `-0.919` n `8`; equity avg `-0.6475` n `142`; fx avg `0.0018` n `6`; index avg `-0.0482` n `26`; metal avg `-0.2065` n `20`; unknown avg `11.6352` n `875`
- 24h: commodity avg `0.0864` n `12`; crypto_alt avg `2.0861` n `234`; crypto_major avg `1.8252` n `8`; equity avg `-0.061` n `142`; fx avg `0.0712` n `6`; index avg `0.1247` n `26`; metal avg `-0.0085` n `20`; unknown avg `4.3106` n `820`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
