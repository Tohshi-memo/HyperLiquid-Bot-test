# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T12:52:25.131534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `13`; crypto_alt avg `-0.1556` n `237`; crypto_major avg `-0.077` n `8`; equity avg `0.0097` n `151`; fx avg `-0.0065` n `6`; index avg `-0.0092` n `26`; metal avg `0.0019` n `20`; unknown avg `0.4321` n `1193`
- 1h: commodity avg `-0.0225` n `13`; crypto_alt avg `0.1256` n `237`; crypto_major avg `-0.0086` n `8`; equity avg `0.0768` n `151`; fx avg `0.0033` n `6`; index avg `-0.008` n `26`; metal avg `0.0046` n `20`; unknown avg `0.1177` n `1185`
- 4h: commodity avg `-0.0015` n `13`; crypto_alt avg `0.3408` n `237`; crypto_major avg `0.343` n `8`; equity avg `0.1416` n `151`; fx avg `0.0014` n `6`; index avg `0.0016` n `26`; metal avg `0.0238` n `20`; unknown avg `4.4202` n `1129`
- 24h: commodity avg `0.0634` n `13`; crypto_alt avg `-1.6543` n `236`; crypto_major avg `0.0267` n `8`; equity avg `-0.4392` n `151`; fx avg `-0.0455` n `6`; index avg `-0.0581` n `26`; metal avg `-0.0331` n `20`; unknown avg `1.7874` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2072`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.138`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1326`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0753`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
