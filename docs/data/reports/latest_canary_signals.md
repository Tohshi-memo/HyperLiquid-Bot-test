# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T01:52:27.458268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `13`; crypto_alt avg `0.0014` n `236`; crypto_major avg `-0.0056` n `8`; equity avg `-0.0395` n `151`; fx avg `-0.0118` n `6`; index avg `0.0128` n `26`; metal avg `0.0307` n `20`; unknown avg `0.1005` n `1136`
- 1h: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.3004` n `236`; crypto_major avg `-0.1991` n `8`; equity avg `0.0634` n `151`; fx avg `0.0117` n `6`; index avg `0.0082` n `26`; metal avg `0.0293` n `20`; unknown avg `0.0234` n `1134`
- 4h: commodity avg `-0.032` n `13`; crypto_alt avg `-0.2804` n `236`; crypto_major avg `-0.5027` n `8`; equity avg `-0.2294` n `151`; fx avg `0.0622` n `6`; index avg `-0.0533` n `26`; metal avg `-0.0761` n `20`; unknown avg `-0.1078` n `1096`
- 24h: commodity avg `0.0112` n `13`; crypto_alt avg `0.9869` n `236`; crypto_major avg `0.4704` n `8`; equity avg `1.7212` n `151`; fx avg `0.0408` n `6`; index avg `0.3064` n `26`; metal avg `0.2039` n `20`; unknown avg `25.6085` n `910`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.091`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0876`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0778`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0643`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0643`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
