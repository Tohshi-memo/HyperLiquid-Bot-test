# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T13:52:31.915763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.2475` n `234`; crypto_major avg `-0.0697` n `8`; equity avg `-0.2879` n `141`; fx avg `0.0261` n `6`; index avg `-0.025` n `26`; metal avg `0.0635` n `20`; unknown avg `2.3016` n `960`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.5894` n `234`; crypto_major avg `-0.2803` n `8`; equity avg `-0.596` n `141`; fx avg `0.0037` n `6`; index avg `-0.0958` n `26`; metal avg `0.0355` n `20`; unknown avg `45.8322` n `958`
- 4h: commodity avg `-0.236` n `12`; crypto_alt avg `1.461` n `234`; crypto_major avg `1.2493` n `8`; equity avg `-0.1136` n `141`; fx avg `0.0177` n `6`; index avg `-0.0042` n `26`; metal avg `0.0023` n `20`; unknown avg `183.2709` n `952`
- 24h: commodity avg `-0.2997` n `12`; crypto_alt avg `-2.442` n `234`; crypto_major avg `-1.7317` n `8`; equity avg `-2.8857` n `141`; fx avg `0.0204` n `6`; index avg `-0.2503` n `26`; metal avg `-0.9023` n `20`; unknown avg `7.6605` n `812`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
