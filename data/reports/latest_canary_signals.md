# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T02:07:26.046978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.0707` n `233`; crypto_major avg `0.0658` n `8`; equity avg `0.078` n `134`; fx avg `0.0012` n `6`; index avg `0.0251` n `26`; metal avg `0.0124` n `20`; unknown avg `-0.0766` n `795`
- 1h: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.0391` n `233`; crypto_major avg `0.0049` n `8`; equity avg `0.0379` n `134`; fx avg `-0.0191` n `6`; index avg `0.0107` n `26`; metal avg `-0.0127` n `20`; unknown avg `-0.1694` n `795`
- 4h: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.0152` n `233`; crypto_major avg `0.4149` n `8`; equity avg `0.4258` n `134`; fx avg `-0.0167` n `6`; index avg `0.1051` n `26`; metal avg `0.0999` n `20`; unknown avg `1.0228` n `765`
- 24h: commodity avg `0.1741` n `12`; crypto_alt avg `-1.1459` n `232`; crypto_major avg `0.1786` n `8`; equity avg `0.3882` n `134`; fx avg `0.0571` n `6`; index avg `-0.1478` n `26`; metal avg `-0.4294` n `20`; unknown avg `0.6428` n `683`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
