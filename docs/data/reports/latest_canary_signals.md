# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T15:52:34.751275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.0182` n `238`; crypto_major avg `-0.0932` n `8`; equity avg `-0.0234` n `156`; fx avg `-0.0069` n `6`; index avg `-0.0017` n `27`; metal avg `-0.0038` n `20`; unknown avg `-0.1281` n `1260`
- 1h: commodity avg `0.0158` n `13`; crypto_alt avg `0.7029` n `238`; crypto_major avg `0.2034` n `8`; equity avg `-0.0083` n `156`; fx avg `-0.0108` n `6`; index avg `-0.0081` n `27`; metal avg `0.0067` n `20`; unknown avg `0.2409` n `1250`
- 4h: commodity avg `-0.0971` n `13`; crypto_alt avg `0.9696` n `238`; crypto_major avg `-0.0091` n `8`; equity avg `0.015` n `156`; fx avg `-0.0078` n `6`; index avg `-0.0078` n `27`; metal avg `0.016` n `20`; unknown avg `-0.0955` n `1242`
- 24h: commodity avg `-0.3487` n `13`; crypto_alt avg `1.3922` n `238`; crypto_major avg `-0.246` n `8`; equity avg `0.0655` n `156`; fx avg `0.0172` n `6`; index avg `-0.0729` n `27`; metal avg `0.0039` n `20`; unknown avg `1.1102` n `1089`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
