# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T01:37:14.418899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.0229` n `228`; crypto_major avg `-0.1721` n `8`; equity avg `-0.0154` n `66`; fx avg `0.0033` n `6`; index avg `0.0447` n `23`; metal avg `-0.0049` n `18`; unknown avg `0.5052` n `384`
- 1h: commodity avg `-0.1708` n `12`; crypto_alt avg `0.3301` n `228`; crypto_major avg `0.3763` n `8`; equity avg `0.422` n `66`; fx avg `0.0339` n `6`; index avg `0.2227` n `23`; metal avg `0.5334` n `18`; unknown avg `1.0822` n `384`
- 4h: commodity avg `-0.1447` n `12`; crypto_alt avg `0.6536` n `228`; crypto_major avg `1.1945` n `8`; equity avg `0.4771` n `66`; fx avg `0.0715` n `6`; index avg `0.181` n `23`; metal avg `0.4886` n `18`; unknown avg `3.1702` n `384`
- 24h: commodity avg `-2.482` n `12`; crypto_alt avg `4.0119` n `228`; crypto_major avg `4.0391` n `8`; equity avg `2.5406` n `66`; fx avg `-0.0104` n `6`; index avg `1.6719` n `23`; metal avg `2.4229` n `18`; unknown avg `4.7536` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
