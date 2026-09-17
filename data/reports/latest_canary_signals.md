# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T06:52:30.161257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.0493` n `234`; crypto_major avg `0.006` n `8`; equity avg `0.0288` n `137`; fx avg `0.0108` n `6`; index avg `0.006` n `27`; metal avg `0.008` n `20`; unknown avg `0.7453` n `921`
- 1h: commodity avg `-0.125` n `12`; crypto_alt avg `0.2481` n `234`; crypto_major avg `0.1526` n `8`; equity avg `0.2078` n `137`; fx avg `0.0096` n `6`; index avg `0.0705` n `27`; metal avg `0.051` n `20`; unknown avg `-0.0511` n `899`
- 4h: commodity avg `-0.2193` n `12`; crypto_alt avg `0.7878` n `234`; crypto_major avg `0.1184` n `8`; equity avg `0.0973` n `137`; fx avg `0.0194` n `6`; index avg `0.0186` n `27`; metal avg `0.1774` n `20`; unknown avg `0.5303` n `891`
- 24h: commodity avg `-0.541` n `12`; crypto_alt avg `2.8282` n `234`; crypto_major avg `1.4532` n `8`; equity avg `1.0009` n `137`; fx avg `0.0316` n `6`; index avg `0.0518` n `27`; metal avg `-0.166` n `20`; unknown avg `0.1125` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
