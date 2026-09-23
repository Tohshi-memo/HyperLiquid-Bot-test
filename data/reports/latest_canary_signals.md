# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T11:07:37.670922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `12`; crypto_alt avg `-0.1367` n `234`; crypto_major avg `0.0899` n `8`; equity avg `-0.1585` n `140`; fx avg `0.0194` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0081` n `20`; unknown avg `7.4074` n `944`
- 1h: commodity avg `0.102` n `12`; crypto_alt avg `-0.2058` n `234`; crypto_major avg `0.0582` n `8`; equity avg `-0.162` n `140`; fx avg `0.0174` n `6`; index avg `-0.0206` n `26`; metal avg `-0.0477` n `20`; unknown avg `7.8237` n `944`
- 4h: commodity avg `0.2327` n `12`; crypto_alt avg `-0.5365` n `234`; crypto_major avg `-0.9795` n `8`; equity avg `-0.2284` n `140`; fx avg `-0.014` n `6`; index avg `-0.0567` n `26`; metal avg `-0.1675` n `20`; unknown avg `3.6731` n `937`
- 24h: commodity avg `0.6655` n `12`; crypto_alt avg `4.064` n `234`; crypto_major avg `0.9622` n `8`; equity avg `0.6008` n `140`; fx avg `0.0256` n `6`; index avg `0.0335` n `26`; metal avg `-0.1241` n `20`; unknown avg `4.5849` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
