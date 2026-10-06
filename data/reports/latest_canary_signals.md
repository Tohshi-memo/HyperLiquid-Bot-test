# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T15:52:29.819964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0614` n `13`; crypto_alt avg `-0.2653` n `235`; crypto_major avg `-0.2547` n `8`; equity avg `0.0699` n `150`; fx avg `-0.014` n `6`; index avg `0.0056` n `26`; metal avg `0.0148` n `20`; unknown avg `1.2318` n `1076`
- 1h: commodity avg `0.1621` n `13`; crypto_alt avg `-0.2159` n `235`; crypto_major avg `-0.408` n `8`; equity avg `0.0548` n `150`; fx avg `0.019` n `6`; index avg `0.0148` n `26`; metal avg `0.181` n `20`; unknown avg `0.9537` n `1070`
- 4h: commodity avg `0.285` n `13`; crypto_alt avg `-0.1021` n `235`; crypto_major avg `-0.284` n `8`; equity avg `0.2797` n `150`; fx avg `-0.0081` n `6`; index avg `-0.0197` n `26`; metal avg `-0.0631` n `20`; unknown avg `5.0963` n `1018`
- 24h: commodity avg `-0.3714` n `13`; crypto_alt avg `0.6635` n `235`; crypto_major avg `0.4985` n `8`; equity avg `0.9007` n `149`; fx avg `0.1121` n `6`; index avg `0.1552` n `26`; metal avg `0.0264` n `20`; unknown avg `381.3585` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
