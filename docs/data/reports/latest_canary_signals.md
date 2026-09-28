# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T00:07:31.202525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.1753` n `234`; crypto_major avg `-0.1955` n `8`; equity avg `0.0922` n `141`; fx avg `0.0495` n `6`; index avg `0.0658` n `26`; metal avg `-0.0451` n `20`; unknown avg `-0.0912` n `954`
- 1h: commodity avg `-0.0019` n `12`; crypto_alt avg `0.5836` n `234`; crypto_major avg `0.3531` n `8`; equity avg `0.1275` n `141`; fx avg `0.0385` n `6`; index avg `0.1039` n `26`; metal avg `-0.0218` n `20`; unknown avg `2.4102` n `954`
- 4h: commodity avg `-0.3113` n `12`; crypto_alt avg `-0.1906` n `234`; crypto_major avg `-0.4375` n `8`; equity avg `-0.2755` n `141`; fx avg `0.0191` n `6`; index avg `0.0036` n `26`; metal avg `-0.2055` n `20`; unknown avg `2.0216` n `886`
- 24h: commodity avg `-0.464` n `12`; crypto_alt avg `0.9406` n `234`; crypto_major avg `-0.0406` n `8`; equity avg `0.0707` n `141`; fx avg `0.0161` n `6`; index avg `0.04` n `26`; metal avg `-0.215` n `20`; unknown avg `10.3161` n `827`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
