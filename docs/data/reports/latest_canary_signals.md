# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T05:22:25.550471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `13`; crypto_alt avg `-0.0073` n `238`; crypto_major avg `-0.0129` n `8`; equity avg `-0.0051` n `156`; fx avg `0.0` n `6`; index avg `0.0018` n `27`; metal avg `0.0001` n `20`; unknown avg `-0.0311` n `1262`
- 1h: commodity avg `-0.0239` n `13`; crypto_alt avg `0.0122` n `238`; crypto_major avg `0.0685` n `8`; equity avg `0.0714` n `156`; fx avg `-0.0013` n `6`; index avg `0.004` n `27`; metal avg `0.0007` n `20`; unknown avg `0.2023` n `1256`
- 4h: commodity avg `0.0321` n `13`; crypto_alt avg `0.1246` n `238`; crypto_major avg `-0.0069` n `8`; equity avg `0.1828` n `156`; fx avg `-0.0055` n `6`; index avg `0.0296` n `27`; metal avg `0.0029` n `20`; unknown avg `1.1541` n `1238`
- 24h: commodity avg `-0.0102` n `13`; crypto_alt avg `0.6408` n `238`; crypto_major avg `0.3208` n `8`; equity avg `0.2407` n `156`; fx avg `0.0075` n `6`; index avg `0.0011` n `27`; metal avg `0.0513` n `20`; unknown avg `2.8152` n `996`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
