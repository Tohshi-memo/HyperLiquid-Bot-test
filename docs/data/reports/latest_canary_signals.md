# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T06:37:26.068586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0199` n `13`; crypto_alt avg `-0.0761` n `236`; crypto_major avg `-0.0372` n `8`; equity avg `-0.007` n `151`; fx avg `-0.006` n `6`; index avg `-0.0031` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.0259` n `1193`
- 1h: commodity avg `-0.0679` n `13`; crypto_alt avg `-0.0109` n `236`; crypto_major avg `0.0402` n `8`; equity avg `0.0229` n `151`; fx avg `0.0001` n `6`; index avg `0.0037` n `26`; metal avg `0.0162` n `20`; unknown avg `-0.0271` n `1175`
- 4h: commodity avg `-0.075` n `13`; crypto_alt avg `0.3536` n `236`; crypto_major avg `0.403` n `8`; equity avg `0.2199` n `151`; fx avg `-0.0038` n `6`; index avg `0.0472` n `26`; metal avg `0.0138` n `20`; unknown avg `1.3377` n `1169`
- 24h: commodity avg `0.5787` n `13`; crypto_alt avg `-1.7539` n `236`; crypto_major avg `-1.2862` n `8`; equity avg `-3.6957` n `151`; fx avg `0.0669` n `6`; index avg `-0.5699` n `26`; metal avg `-0.1907` n `20`; unknown avg `40.3626` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1805`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1199`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.075`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
