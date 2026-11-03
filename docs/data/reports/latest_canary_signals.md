# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T22:07:58.315306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `13`; crypto_alt avg `-0.0586` n `239`; crypto_major avg `-0.0819` n `8`; equity avg `-0.089` n `158`; fx avg `-0.0227` n `6`; index avg `0.005` n `27`; metal avg `0.0176` n `20`; unknown avg `158.4183` n `1258`
- 1h: commodity avg `0.0151` n `13`; crypto_alt avg `0.2266` n `239`; crypto_major avg `0.0216` n `8`; equity avg `0.6838` n `158`; fx avg `-0.0169` n `6`; index avg `0.0909` n `27`; metal avg `0.0566` n `20`; unknown avg `159.4308` n `1257`
- 4h: commodity avg `0.2235` n `13`; crypto_alt avg `0.0901` n `239`; crypto_major avg `-0.208` n `8`; equity avg `0.5505` n `158`; fx avg `-0.0115` n `6`; index avg `0.0377` n `27`; metal avg `-0.0551` n `20`; unknown avg `19.7582` n `1213`
- 24h: commodity avg `0.4057` n `13`; crypto_alt avg `0.9879` n `239`; crypto_major avg `1.2487` n `8`; equity avg `2.3177` n `158`; fx avg `0.0552` n `6`; index avg `0.2313` n `27`; metal avg `-0.4865` n `20`; unknown avg `-1.0314` n `1063`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
