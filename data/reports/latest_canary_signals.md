# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T05:37:25.630435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0266` n `13`; crypto_alt avg `0.0388` n `238`; crypto_major avg `0.0334` n `8`; equity avg `-0.0113` n `156`; fx avg `-0.0044` n `6`; index avg `0.0005` n `27`; metal avg `-0.0031` n `20`; unknown avg `0.2425` n `1262`
- 1h: commodity avg `0.0014` n `13`; crypto_alt avg `0.0935` n `238`; crypto_major avg `0.1014` n `8`; equity avg `0.03` n `156`; fx avg `0.0048` n `6`; index avg `-0.0004` n `27`; metal avg `-0.0044` n `20`; unknown avg `0.4824` n `1256`
- 4h: commodity avg `0.0554` n `13`; crypto_alt avg `0.0664` n `238`; crypto_major avg `-0.076` n `8`; equity avg `0.1553` n `156`; fx avg `-0.0111` n `6`; index avg `0.0301` n `27`; metal avg `-0.0015` n `20`; unknown avg `0.7307` n `1240`
- 24h: commodity avg `0.0106` n `13`; crypto_alt avg `0.6368` n `238`; crypto_major avg `0.3335` n `8`; equity avg `0.2261` n `156`; fx avg `0.0007` n `6`; index avg `-0.0089` n `27`; metal avg `0.0499` n `20`; unknown avg `2.1256` n `996`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
