# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T12:22:27.376246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1408` n `13`; crypto_alt avg `0.1329` n `236`; crypto_major avg `0.0305` n `8`; equity avg `-0.0345` n `151`; fx avg `-0.0082` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0064` n `20`; unknown avg `-0.0379` n `1136`
- 1h: commodity avg `-0.1289` n `13`; crypto_alt avg `-0.0017` n `236`; crypto_major avg `-0.4779` n `8`; equity avg `-0.1555` n `151`; fx avg `-0.0094` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0539` n `20`; unknown avg `19.8943` n `1128`
- 4h: commodity avg `-0.0549` n `13`; crypto_alt avg `0.4838` n `236`; crypto_major avg `0.2372` n `8`; equity avg `-0.4703` n `151`; fx avg `0.0343` n `6`; index avg `-0.0188` n `26`; metal avg `-0.0342` n `20`; unknown avg `2.2396` n `1126`
- 24h: commodity avg `-0.0952` n `13`; crypto_alt avg `4.7715` n `236`; crypto_major avg `2.4894` n `8`; equity avg `2.4388` n `151`; fx avg `0.0113` n `6`; index avg `0.3313` n `26`; metal avg `0.3029` n `20`; unknown avg `25.3521` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0973`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0915`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0846`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0743`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
