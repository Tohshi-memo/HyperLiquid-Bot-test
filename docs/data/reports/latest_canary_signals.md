# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T00:37:35.031862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.049` n `13`; crypto_alt avg `-0.0671` n `235`; crypto_major avg `0.022` n `8`; equity avg `-0.0097` n `150`; fx avg `-0.01` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0318` n `20`; unknown avg `0.0038` n `1134`
- 1h: commodity avg `-0.182` n `13`; crypto_alt avg `-0.1264` n `235`; crypto_major avg `0.0508` n `8`; equity avg `0.1342` n `150`; fx avg `-0.0318` n `6`; index avg `-0.0188` n `26`; metal avg `0.0484` n `20`; unknown avg `-0.0961` n `1126`
- 4h: commodity avg `-0.4448` n `13`; crypto_alt avg `0.0187` n `235`; crypto_major avg `0.1085` n `8`; equity avg `0.278` n `150`; fx avg `-0.04` n `6`; index avg `0.0377` n `26`; metal avg `0.0757` n `20`; unknown avg `-0.1829` n `1098`
- 24h: commodity avg `-0.3418` n `13`; crypto_alt avg `2.2061` n `235`; crypto_major avg `1.0114` n `8`; equity avg `0.5883` n `150`; fx avg `-0.018` n `6`; index avg `0.0688` n `26`; metal avg `0.1552` n `20`; unknown avg `0.5786` n `957`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
