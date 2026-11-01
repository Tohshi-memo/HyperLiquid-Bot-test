# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T10:07:22.987261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `13`; crypto_alt avg `-0.0274` n `238`; crypto_major avg `0.0052` n `8`; equity avg `0.0083` n `156`; fx avg `-0.0006` n `6`; index avg `-0.0113` n `27`; metal avg `0.0016` n `20`; unknown avg `-0.0053` n `1257`
- 1h: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.0668` n `238`; crypto_major avg `-0.1747` n `8`; equity avg `-0.0083` n `156`; fx avg `-0.0026` n `6`; index avg `-0.007` n `27`; metal avg `-0.001` n `20`; unknown avg `0.0129` n `1257`
- 4h: commodity avg `-0.0079` n `13`; crypto_alt avg `-0.1909` n `238`; crypto_major avg `0.0213` n `8`; equity avg `0.1528` n `156`; fx avg `-0.0086` n `6`; index avg `0.0152` n `27`; metal avg `0.0179` n `20`; unknown avg `0.6193` n `1240`
- 24h: commodity avg `-0.0078` n `13`; crypto_alt avg `0.8604` n `238`; crypto_major avg `0.7499` n `8`; equity avg `0.5047` n `156`; fx avg `-0.0177` n `6`; index avg `0.0219` n `27`; metal avg `0.0559` n `20`; unknown avg `2.6548` n `996`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
