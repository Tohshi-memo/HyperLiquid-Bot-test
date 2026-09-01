# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T00:22:25.849362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `0.4056` n `232`; crypto_major avg `0.1504` n `8`; equity avg `0.0447` n `129`; fx avg `-0.0474` n `6`; index avg `0.0116` n `26`; metal avg `0.0022` n `20`; unknown avg `-0.0556` n `793`
- 1h: commodity avg `0.0539` n `12`; crypto_alt avg `0.6458` n `232`; crypto_major avg `0.2824` n `8`; equity avg `0.0725` n `129`; fx avg `-0.0265` n `6`; index avg `0.0224` n `26`; metal avg `0.1421` n `20`; unknown avg `-0.1906` n `791`
- 4h: commodity avg `0.0975` n `12`; crypto_alt avg `0.5063` n `232`; crypto_major avg `-0.2948` n `8`; equity avg `0.06` n `129`; fx avg `-0.0197` n `6`; index avg `0.0103` n `26`; metal avg `0.1099` n `20`; unknown avg `0.8006` n `785`
- 24h: commodity avg `0.6491` n `12`; crypto_alt avg `2.1751` n `231`; crypto_major avg `1.5399` n `8`; equity avg `1.0856` n `129`; fx avg `-0.1345` n `6`; index avg `0.1353` n `26`; metal avg `-0.1857` n `20`; unknown avg `0.1993` n `740`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
