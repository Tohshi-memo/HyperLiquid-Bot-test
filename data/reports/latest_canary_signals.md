# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T15:52:25.084949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.1016` n `228`; crypto_major avg `0.0684` n `8`; equity avg `0.1093` n `67`; fx avg `0.0049` n `6`; index avg `0.0362` n `23`; metal avg `0.156` n `18`; unknown avg `0.0506` n `385`
- 1h: commodity avg `0.1123` n `12`; crypto_alt avg `0.6959` n `228`; crypto_major avg `0.4251` n `8`; equity avg `0.1433` n `67`; fx avg `-0.0096` n `6`; index avg `0.024` n `23`; metal avg `0.2981` n `18`; unknown avg `1.0627` n `385`
- 4h: commodity avg `0.4254` n `12`; crypto_alt avg `1.1448` n `228`; crypto_major avg `1.1586` n `8`; equity avg `0.3364` n `67`; fx avg `-0.0765` n `6`; index avg `-0.0831` n `23`; metal avg `0.4843` n `18`; unknown avg `1.5681` n `385`
- 24h: commodity avg `0.87` n `12`; crypto_alt avg `1.302` n `228`; crypto_major avg `2.2959` n `8`; equity avg `0.7243` n `66`; fx avg `-0.0022` n `6`; index avg `0.0782` n `23`; metal avg `-0.4478` n `18`; unknown avg `8.1616` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
