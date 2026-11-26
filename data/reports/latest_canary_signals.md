# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T09:22:29.536921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0426` n `13`; crypto_alt avg `0.029` n `239`; crypto_major avg `-0.1948` n `8`; equity avg `-0.2499` n `168`; fx avg `0.017` n `6`; index avg `-0.0451` n `27`; metal avg `-0.0439` n `20`; unknown avg `0.0012` n `1265`
- 1h: commodity avg `-0.1877` n `13`; crypto_alt avg `0.2032` n `239`; crypto_major avg `0.129` n `8`; equity avg `0.1168` n `168`; fx avg `0.0172` n `6`; index avg `-0.0129` n `27`; metal avg `0.1114` n `20`; unknown avg `170.0886` n `1193`
- 4h: commodity avg `-0.3514` n `13`; crypto_alt avg `0.0229` n `239`; crypto_major avg `-0.4961` n `8`; equity avg `-0.7627` n `168`; fx avg `0.0559` n `6`; index avg `-0.1067` n `27`; metal avg `-0.18` n `20`; unknown avg `177.9035` n `1133`
- 24h: commodity avg `0.3843` n `13`; crypto_alt avg `3.2819` n `239`; crypto_major avg `3.5227` n `8`; equity avg `3.3788` n `168`; fx avg `0.0853` n `6`; index avg `0.2454` n `27`; metal avg `0.7308` n `20`; unknown avg `0.0027` n `995`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
