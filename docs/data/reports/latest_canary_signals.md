# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T15:07:40.388767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.076` n `238`; crypto_major avg `0.0104` n `8`; equity avg `0.0227` n `156`; fx avg `-0.0013` n `6`; index avg `0.0069` n `27`; metal avg `0.0006` n `20`; unknown avg `-0.2279` n `1257`
- 1h: commodity avg `0.0179` n `13`; crypto_alt avg `-0.1559` n `238`; crypto_major avg `-0.0019` n `8`; equity avg `0.0086` n `156`; fx avg `0.002` n `6`; index avg `0.0274` n `27`; metal avg `-0.0061` n `20`; unknown avg `3.1016` n `1257`
- 4h: commodity avg `0.0486` n `13`; crypto_alt avg `0.1027` n `238`; crypto_major avg `0.0706` n `8`; equity avg `0.0129` n `156`; fx avg `0.0166` n `6`; index avg `0.042` n `27`; metal avg `-0.0016` n `20`; unknown avg `-0.1095` n `1251`
- 24h: commodity avg `0.0831` n `13`; crypto_alt avg `0.3244` n `238`; crypto_major avg `0.6711` n `8`; equity avg `0.4773` n `156`; fx avg `-0.0081` n `6`; index avg `0.0769` n `27`; metal avg `0.0553` n `20`; unknown avg `3.4219` n `1018`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
