# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T13:22:25.218546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.6076` n `12`; crypto_alt avg `0.2203` n `228`; crypto_major avg `-0.0357` n `8`; equity avg `-0.4059` n `69`; fx avg `0.0076` n `6`; index avg `-0.1552` n `23`; metal avg `-0.6474` n `18`; unknown avg `0.1399` n `422`
- 1h: commodity avg `0.4578` n `12`; crypto_alt avg `-0.1811` n `228`; crypto_major avg `-0.2806` n `8`; equity avg `-0.4065` n `69`; fx avg `-0.0189` n `6`; index avg `-0.1639` n `23`; metal avg `-0.5932` n `18`; unknown avg `0.9301` n `422`
- 4h: commodity avg `-0.4776` n `12`; crypto_alt avg `-0.5944` n `228`; crypto_major avg `-0.4626` n `8`; equity avg `-0.8373` n `69`; fx avg `-0.0192` n `6`; index avg `-0.3356` n `23`; metal avg `-0.7975` n `18`; unknown avg `2.2163` n `416`
- 24h: commodity avg `0.6818` n `12`; crypto_alt avg `-1.1871` n `228`; crypto_major avg `-1.4434` n `8`; equity avg `-0.9475` n `69`; fx avg `-0.0176` n `6`; index avg `0.2445` n `23`; metal avg `-0.5307` n `18`; unknown avg `4.1334` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2889`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
