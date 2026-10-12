# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T16:07:38.649729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `13`; crypto_alt avg `0.1889` n `235`; crypto_major avg `0.2007` n `8`; equity avg `0.1493` n `151`; fx avg `-0.0028` n `6`; index avg `0.0247` n `26`; metal avg `0.0014` n `20`; unknown avg `0.9989` n `1126`
- 1h: commodity avg `0.023` n `13`; crypto_alt avg `0.1459` n `235`; crypto_major avg `0.2721` n `8`; equity avg `0.2576` n `151`; fx avg `-0.0363` n `6`; index avg `0.0591` n `26`; metal avg `0.0028` n `20`; unknown avg `1.9957` n `1126`
- 4h: commodity avg `0.3444` n `13`; crypto_alt avg `-1.5538` n `235`; crypto_major avg `-0.8822` n `8`; equity avg `-1.3241` n `151`; fx avg `-0.0429` n `6`; index avg `-0.0622` n `26`; metal avg `-0.1185` n `20`; unknown avg `-0.0425` n `1074`
- 24h: commodity avg `0.5131` n `13`; crypto_alt avg `-2.2847` n `235`; crypto_major avg `-1.4552` n `8`; equity avg `-2.9139` n `151`; fx avg `-0.1541` n `6`; index avg `-0.2486` n `26`; metal avg `-0.1183` n `20`; unknown avg `-0.4317` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2186`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2061`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1162`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1049`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0879`, n `666`, weak_sample_signal
