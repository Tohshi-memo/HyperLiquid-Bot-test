# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T05:22:27.714027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `13`; crypto_alt avg `0.0116` n `236`; crypto_major avg `-0.0679` n `8`; equity avg `-0.0707` n `151`; fx avg `-0.0257` n `6`; index avg `-0.0093` n `26`; metal avg `0.0141` n `20`; unknown avg `1.1311` n `1136`
- 1h: commodity avg `0.0167` n `13`; crypto_alt avg `0.1866` n `236`; crypto_major avg `0.2416` n `8`; equity avg `0.113` n `151`; fx avg `-0.0576` n `6`; index avg `0.0085` n `26`; metal avg `-0.0542` n `20`; unknown avg `2.8589` n `1132`
- 4h: commodity avg `-0.0188` n `13`; crypto_alt avg `0.1673` n `236`; crypto_major avg `0.2538` n `8`; equity avg `0.6406` n `151`; fx avg `-0.0362` n `6`; index avg `0.0863` n `26`; metal avg `0.2303` n `20`; unknown avg `0.9196` n `1124`
- 24h: commodity avg `0.0007` n `13`; crypto_alt avg `4.0015` n `236`; crypto_major avg `2.1561` n `8`; equity avg `2.5599` n `151`; fx avg `0.0011` n `6`; index avg `0.3869` n `26`; metal avg `0.5151` n `20`; unknown avg `25.6675` n `906`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0931`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.075`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0722`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0682`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
