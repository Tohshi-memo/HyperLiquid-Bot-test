# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T17:52:28.512423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `13`; crypto_alt avg `-0.0788` n `238`; crypto_major avg `0.1499` n `8`; equity avg `0.0342` n `156`; fx avg `-0.0087` n `6`; index avg `0.0014` n `27`; metal avg `-0.0068` n `20`; unknown avg `0.0849` n `1262`
- 1h: commodity avg `-0.0151` n `13`; crypto_alt avg `-0.4585` n `238`; crypto_major avg `0.1401` n `8`; equity avg `0.0373` n `156`; fx avg `-0.0054` n `6`; index avg `-0.0015` n `27`; metal avg `-0.0097` n `20`; unknown avg `-0.6348` n `1256`
- 4h: commodity avg `-0.0794` n `13`; crypto_alt avg `0.3824` n `238`; crypto_major avg `0.2758` n `8`; equity avg `0.1572` n `156`; fx avg `-0.0119` n `6`; index avg `0.0097` n `27`; metal avg `0.0169` n `20`; unknown avg `135.1047` n `1236`
- 24h: commodity avg `-0.4632` n `13`; crypto_alt avg `1.1797` n `238`; crypto_major avg `0.3616` n `8`; equity avg `1.2937` n `156`; fx avg `0.0018` n `6`; index avg `0.0426` n `27`; metal avg `0.1076` n `20`; unknown avg `1.2753` n `1081`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
