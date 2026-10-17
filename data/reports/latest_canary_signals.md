# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T02:22:25.471899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `13`; crypto_alt avg `0.0114` n `236`; crypto_major avg `-0.0517` n `8`; equity avg `-0.01` n `151`; fx avg `0.0127` n `6`; index avg `0.0054` n `26`; metal avg `0.0047` n `20`; unknown avg `-0.0992` n `1193`
- 1h: commodity avg `-0.0028` n `13`; crypto_alt avg `0.0991` n `236`; crypto_major avg `0.0491` n `8`; equity avg `0.0026` n `151`; fx avg `0.0025` n `6`; index avg `0.0051` n `26`; metal avg `-0.007` n `20`; unknown avg `-0.1609` n `1189`
- 4h: commodity avg `0.1494` n `13`; crypto_alt avg `-0.0278` n `236`; crypto_major avg `-0.2992` n `8`; equity avg `0.253` n `151`; fx avg `0.007` n `6`; index avg `0.0233` n `26`; metal avg `-0.0225` n `20`; unknown avg `0.592` n `1183`
- 24h: commodity avg `0.7036` n `13`; crypto_alt avg `-1.2462` n `236`; crypto_major avg `-1.2281` n `8`; equity avg `-3.8475` n `151`; fx avg `-0.0258` n `6`; index avg `-0.6315` n `26`; metal avg `-0.0922` n `20`; unknown avg `40.1724` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1701`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0768`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0708`, n `666`, weak_sample_signal
