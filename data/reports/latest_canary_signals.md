# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T08:37:31.792063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0557` n `13`; crypto_alt avg `-0.0908` n `236`; crypto_major avg `-0.053` n `8`; equity avg `-0.0077` n `151`; fx avg `-0.0139` n `6`; index avg `0.0175` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.0235` n `1193`
- 1h: commodity avg `0.0591` n `13`; crypto_alt avg `-0.132` n `236`; crypto_major avg `-0.1166` n `8`; equity avg `-0.0345` n `151`; fx avg `-0.0112` n `6`; index avg `0.0137` n `26`; metal avg `-0.0023` n `20`; unknown avg `-0.0867` n `1175`
- 4h: commodity avg `-0.1793` n `13`; crypto_alt avg `-0.6679` n `236`; crypto_major avg `0.0586` n `8`; equity avg `0.0361` n `151`; fx avg `-0.0079` n `6`; index avg `0.0484` n `26`; metal avg `-0.009` n `20`; unknown avg `-0.0383` n `1157`
- 24h: commodity avg `0.4781` n `13`; crypto_alt avg `-2.2091` n `236`; crypto_major avg `-1.3995` n `8`; equity avg `-3.8639` n `151`; fx avg `0.0402` n `6`; index avg `-0.5701` n `26`; metal avg `-0.2533` n `20`; unknown avg `8.6795` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1821`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1437`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1235`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0737`, n `666`, weak_sample_signal
