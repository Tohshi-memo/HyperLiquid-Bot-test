# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T13:52:25.933297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0322` n `234`; crypto_major avg `-0.06` n `8`; equity avg `0.0076` n `140`; fx avg `0.0021` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0049` n `20`; unknown avg `1.3545` n `942`
- 1h: commodity avg `0.0007` n `12`; crypto_alt avg `-0.2673` n `234`; crypto_major avg `-0.0995` n `8`; equity avg `0.0145` n `140`; fx avg `0.0011` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0033` n `20`; unknown avg `-0.2641` n `938`
- 4h: commodity avg `0.029` n `12`; crypto_alt avg `0.4436` n `234`; crypto_major avg `0.4225` n `8`; equity avg `0.0371` n `140`; fx avg `-0.0268` n `6`; index avg `0.0014` n `26`; metal avg `0.0281` n `20`; unknown avg `0.509` n `932`
- 24h: commodity avg `-0.1967` n `12`; crypto_alt avg `2.8516` n `234`; crypto_major avg `1.7322` n `8`; equity avg `0.5873` n `140`; fx avg `-0.0223` n `6`; index avg `0.0683` n `26`; metal avg `0.0551` n `20`; unknown avg `1.7862` n `808`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
