# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T01:52:27.748012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0926` n `13`; crypto_alt avg `0.3177` n `235`; crypto_major avg `0.2171` n `8`; equity avg `0.2995` n `150`; fx avg `-0.0057` n `6`; index avg `0.0438` n `26`; metal avg `0.0379` n `20`; unknown avg `0.2272` n `1078`
- 1h: commodity avg `-0.1668` n `13`; crypto_alt avg `0.7619` n `235`; crypto_major avg `0.1725` n `8`; equity avg `0.3869` n `150`; fx avg `-0.0488` n `6`; index avg `0.036` n `26`; metal avg `0.2898` n `20`; unknown avg `0.2949` n `1076`
- 4h: commodity avg `-0.1439` n `13`; crypto_alt avg `0.678` n `235`; crypto_major avg `0.236` n `8`; equity avg `0.5291` n `150`; fx avg `0.0189` n `6`; index avg `0.0879` n `26`; metal avg `0.4126` n `20`; unknown avg `0.4727` n `1069`
- 24h: commodity avg `0.2585` n `13`; crypto_alt avg `-2.6988` n `235`; crypto_major avg `-3.3683` n `8`; equity avg `-2.3446` n `150`; fx avg `0.1182` n `6`; index avg `-0.2777` n `26`; metal avg `0.0661` n `20`; unknown avg `5.7297` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
