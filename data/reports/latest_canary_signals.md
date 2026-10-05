# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T01:22:27.573968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.028` n `13`; crypto_alt avg `0.0237` n `235`; crypto_major avg `0.1201` n `8`; equity avg `0.0552` n `144`; fx avg `-0.0087` n `6`; index avg `0.0073` n `26`; metal avg `-0.0327` n `20`; unknown avg `-0.0633` n `1082`
- 1h: commodity avg `-0.0099` n `13`; crypto_alt avg `0.2748` n `235`; crypto_major avg `0.2895` n `8`; equity avg `0.1574` n `144`; fx avg `-0.0964` n `6`; index avg `0.0089` n `26`; metal avg `0.0426` n `20`; unknown avg `0.5416` n `1068`
- 4h: commodity avg `-0.2072` n `13`; crypto_alt avg `0.8252` n `235`; crypto_major avg `0.4834` n `8`; equity avg `0.4616` n `144`; fx avg `-0.0904` n `6`; index avg `0.0468` n `26`; metal avg `0.1851` n `20`; unknown avg `1.637` n `1006`
- 24h: commodity avg `-0.2952` n `13`; crypto_alt avg `1.51` n `235`; crypto_major avg `1.8669` n `8`; equity avg `0.7068` n `144`; fx avg `-0.0831` n `6`; index avg `0.0441` n `26`; metal avg `0.1879` n `20`; unknown avg `0.8035` n `950`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
