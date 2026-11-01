# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T16:52:32.092400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `13`; crypto_alt avg `0.1119` n `238`; crypto_major avg `0.095` n `8`; equity avg `0.0152` n `156`; fx avg `-0.0014` n `6`; index avg `-0.001` n `27`; metal avg `0.0063` n `20`; unknown avg `-0.0539` n `1263`
- 1h: commodity avg `0.011` n `13`; crypto_alt avg `-0.0683` n `238`; crypto_major avg `0.0448` n `8`; equity avg `0.0436` n `156`; fx avg `0.0082` n `6`; index avg `0.0127` n `27`; metal avg `-0.0017` n `20`; unknown avg `-0.2691` n `1243`
- 4h: commodity avg `-0.0611` n `13`; crypto_alt avg `-0.2084` n `238`; crypto_major avg `0.0558` n `8`; equity avg `0.052` n `156`; fx avg `0.0326` n `6`; index avg `0.0561` n `27`; metal avg `0.0038` n `20`; unknown avg `-0.3777` n `1245`
- 24h: commodity avg `0.009` n `13`; crypto_alt avg `-0.694` n `238`; crypto_major avg `0.1781` n `8`; equity avg `0.4943` n `156`; fx avg `0.0115` n `6`; index avg `0.0945` n `27`; metal avg `0.0446` n `20`; unknown avg `1.5496` n `1010`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
