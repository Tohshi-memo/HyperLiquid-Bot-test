# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T12:52:28.680928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.0972` n `234`; crypto_major avg `-0.0237` n `8`; equity avg `-0.0028` n `141`; fx avg `-0.0011` n `6`; index avg `0.0062` n `26`; metal avg `-0.0027` n `20`; unknown avg `-0.0534` n `962`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `0.0306` n `234`; crypto_major avg `0.2255` n `8`; equity avg `0.0257` n `141`; fx avg `0.0073` n `6`; index avg `0.0029` n `26`; metal avg `-0.0095` n `20`; unknown avg `1.9378` n `954`
- 4h: commodity avg `0.027` n `12`; crypto_alt avg `-0.0952` n `234`; crypto_major avg `0.1925` n `8`; equity avg `0.0163` n `141`; fx avg `-0.0033` n `6`; index avg `-0.0127` n `26`; metal avg `-0.0084` n `20`; unknown avg `1.5948` n `953`
- 24h: commodity avg `0.0315` n `12`; crypto_alt avg `0.9614` n `234`; crypto_major avg `1.0515` n `8`; equity avg `0.3764` n `141`; fx avg `-0.0303` n `6`; index avg `0.0425` n `26`; metal avg `-0.0145` n `20`; unknown avg `63.2659` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
