# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T14:52:31.049528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0603` n `12`; crypto_alt avg `0.0267` n `230`; crypto_major avg `-0.0714` n `8`; equity avg `-0.0794` n `113`; fx avg `0.0076` n `6`; index avg `-0.0195` n `25`; metal avg `0.0755` n `20`; unknown avg `-0.0072` n `787`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.3136` n `230`; crypto_major avg `0.1435` n `8`; equity avg `0.4466` n `113`; fx avg `0.0025` n `6`; index avg `0.0932` n `25`; metal avg `0.0187` n `20`; unknown avg `-0.0157` n `787`
- 4h: commodity avg `-0.1556` n `12`; crypto_alt avg `0.4042` n `230`; crypto_major avg `0.3972` n `8`; equity avg `1.7667` n `113`; fx avg `-0.032` n `6`; index avg `0.2921` n `25`; metal avg `-0.0983` n `20`; unknown avg `0.1186` n `787`
- 24h: commodity avg `-0.4884` n `12`; crypto_alt avg `0.367` n `230`; crypto_major avg `0.6579` n `8`; equity avg `2.0318` n `113`; fx avg `0.0107` n `6`; index avg `0.3227` n `25`; metal avg `-0.4795` n `20`; unknown avg `0.3437` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2277`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1987`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
