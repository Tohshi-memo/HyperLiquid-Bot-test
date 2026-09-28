# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T00:22:27.114311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `0.5413` n `234`; crypto_major avg `0.5893` n `8`; equity avg `0.0573` n `141`; fx avg `0.0339` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0355` n `20`; unknown avg `21.5405` n `962`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `0.8536` n `234`; crypto_major avg `0.6253` n `8`; equity avg `0.1922` n `141`; fx avg `0.0716` n `6`; index avg `0.0817` n `26`; metal avg `-0.0733` n `20`; unknown avg `20.8151` n `954`
- 4h: commodity avg `-0.3332` n `12`; crypto_alt avg `0.4998` n `234`; crypto_major avg `0.2387` n `8`; equity avg `-0.2166` n `141`; fx avg `0.0524` n `6`; index avg `0.0007` n `26`; metal avg `-0.2388` n `20`; unknown avg `2.394` n `886`
- 24h: commodity avg `-0.4476` n `12`; crypto_alt avg `1.5937` n `234`; crypto_major avg `0.6538` n `8`; equity avg `0.1082` n `141`; fx avg `0.0451` n `6`; index avg `0.0373` n `26`; metal avg `-0.2537` n `20`; unknown avg `8.6105` n `827`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
