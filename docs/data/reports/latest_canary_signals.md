# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T10:28:59.130552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0336` n `12`; crypto_alt avg `-0.0714` n `234`; crypto_major avg `-0.1121` n `8`; equity avg `0.0793` n `137`; fx avg `0.0039` n `6`; index avg `0.0197` n `27`; metal avg `0.0274` n `20`; unknown avg `-0.0773` n `921`
- 1h: commodity avg `-0.1209` n `12`; crypto_alt avg `-0.4946` n `234`; crypto_major avg `-0.7213` n `8`; equity avg `0.0523` n `137`; fx avg `0.0266` n `6`; index avg `0.031` n `27`; metal avg `-0.0039` n `20`; unknown avg `0.2118` n `919`
- 4h: commodity avg `-0.1` n `12`; crypto_alt avg `0.3067` n `234`; crypto_major avg `0.1306` n `8`; equity avg `0.8937` n `137`; fx avg `0.0754` n `6`; index avg `0.1514` n `27`; metal avg `0.0323` n `20`; unknown avg `-0.1963` n `911`
- 24h: commodity avg `-0.6289` n `12`; crypto_alt avg `2.9672` n `234`; crypto_major avg `1.3052` n `8`; equity avg `1.5923` n `137`; fx avg `0.1128` n `6`; index avg `0.1508` n `27`; metal avg `-0.1615` n `20`; unknown avg `0.3699` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
