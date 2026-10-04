# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T15:52:36.273841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `13`; crypto_alt avg `-0.091` n `235`; crypto_major avg `0.0656` n `8`; equity avg `-0.0198` n `144`; fx avg `-0.0149` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.3085` n `1078`
- 1h: commodity avg `0.0373` n `13`; crypto_alt avg `-0.2634` n `235`; crypto_major avg `0.1106` n `8`; equity avg `-0.0156` n `144`; fx avg `0.0131` n `6`; index avg `-0.0133` n `26`; metal avg `-0.0082` n `20`; unknown avg `0.3706` n `1076`
- 4h: commodity avg `-0.0567` n `13`; crypto_alt avg `-0.0207` n `235`; crypto_major avg `0.144` n `8`; equity avg `0.0278` n `144`; fx avg `0.0085` n `6`; index avg `-0.0222` n `26`; metal avg `-0.0095` n `20`; unknown avg `0.1227` n `1070`
- 24h: commodity avg `-0.1097` n `13`; crypto_alt avg `0.9482` n `235`; crypto_major avg `0.9438` n `8`; equity avg `0.2393` n `144`; fx avg `0.0334` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.3745` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2038`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
