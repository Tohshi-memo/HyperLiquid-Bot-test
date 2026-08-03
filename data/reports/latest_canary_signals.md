# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T15:07:32.778077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.544` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.0855` n `230`; crypto_major avg `0.0607` n `8`; equity avg `-0.1129` n `102`; fx avg `0.0052` n `6`; index avg `-0.0016` n `25`; metal avg `0.0131` n `20`; unknown avg `0.0211` n `785`
- 1h: commodity avg `0.1133` n `12`; crypto_alt avg `0.0794` n `230`; crypto_major avg `0.512` n `8`; equity avg `1.6324` n `102`; fx avg `-0.0043` n `6`; index avg `0.218` n `25`; metal avg `0.078` n `20`; unknown avg `-0.101` n `785`
- 4h: commodity avg `0.0681` n `12`; crypto_alt avg `1.0074` n `230`; crypto_major avg `1.3183` n `8`; equity avg `2.2122` n `102`; fx avg `-0.0387` n `6`; index avg `0.1416` n `25`; metal avg `-0.2257` n `20`; unknown avg `0.2646` n `785`
- 24h: commodity avg `-0.2615` n `12`; crypto_alt avg `0.1552` n `230`; crypto_major avg `1.0051` n `8`; equity avg `1.5023` n `102`; fx avg `-0.1875` n `6`; index avg `-0.0205` n `25`; metal avg `-0.4534` n `20`; unknown avg `0.2705` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
