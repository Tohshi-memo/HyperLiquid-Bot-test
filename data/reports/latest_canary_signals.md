# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T07:37:32.143263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0699` n `12`; crypto_alt avg `-0.0283` n `233`; crypto_major avg `-0.0287` n `8`; equity avg `0.0179` n `134`; fx avg `-0.0206` n `6`; index avg `0.0036` n `26`; metal avg `0.035` n `20`; unknown avg `0.0579` n `798`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `0.1487` n `233`; crypto_major avg `0.1174` n `8`; equity avg `0.0223` n `134`; fx avg `-0.0034` n `6`; index avg `0.0069` n `26`; metal avg `0.0817` n `20`; unknown avg `0.1754` n `796`
- 4h: commodity avg `0.003` n `12`; crypto_alt avg `1.4398` n `233`; crypto_major avg `1.1218` n `8`; equity avg `0.0948` n `134`; fx avg `-0.0355` n `6`; index avg `-0.007` n `26`; metal avg `0.2746` n `20`; unknown avg `0.9246` n `771`
- 24h: commodity avg `-0.2317` n `12`; crypto_alt avg `0.4678` n `232`; crypto_major avg `1.4069` n `8`; equity avg `1.1479` n `134`; fx avg `-0.1035` n `6`; index avg `0.0583` n `26`; metal avg `0.1035` n `20`; unknown avg `0.4651` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
