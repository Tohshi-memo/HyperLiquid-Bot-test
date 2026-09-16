# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T22:07:34.306444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.4114` n `234`; crypto_major avg `-0.4069` n `8`; equity avg `-0.0594` n `137`; fx avg `-0.0104` n `6`; index avg `-0.0023` n `27`; metal avg `-0.007` n `20`; unknown avg `1.88` n `885`
- 1h: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.4292` n `234`; crypto_major avg `-0.6807` n `8`; equity avg `0.0858` n `137`; fx avg `-0.0028` n `6`; index avg `0.0049` n `27`; metal avg `-0.0252` n `20`; unknown avg `2.8135` n `885`
- 4h: commodity avg `0.0276` n `12`; crypto_alt avg `-0.3125` n `234`; crypto_major avg `-0.8064` n `8`; equity avg `-0.7675` n `137`; fx avg `0.0831` n `6`; index avg `-0.2154` n `27`; metal avg `-0.5003` n `20`; unknown avg `-0.0176` n `797`
- 24h: commodity avg `-0.565` n `12`; crypto_alt avg `0.3671` n `234`; crypto_major avg `0.5644` n `8`; equity avg `0.988` n `137`; fx avg `0.0771` n `6`; index avg `0.0332` n `27`; metal avg `-0.3123` n `20`; unknown avg `-0.5144` n `763`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
