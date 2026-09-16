# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T19:37:28.068633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8401` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0947` n `12`; crypto_alt avg `0.0419` n `234`; crypto_major avg `0.2378` n `8`; equity avg `0.4425` n `137`; fx avg `0.0187` n `6`; index avg `0.0756` n `27`; metal avg `0.1004` n `20`; unknown avg `7.8499` n `909`
- 1h: commodity avg `-0.0776` n `12`; crypto_alt avg `0.5152` n `234`; crypto_major avg `0.5618` n `8`; equity avg `-0.609` n `137`; fx avg `0.0478` n `6`; index avg `-0.1524` n `27`; metal avg `-0.1431` n `20`; unknown avg `6.0829` n `879`
- 4h: commodity avg `-0.1194` n `12`; crypto_alt avg `0.4022` n `234`; crypto_major avg `0.4687` n `8`; equity avg `-1.3714` n `137`; fx avg `0.0433` n `6`; index avg `-0.327` n `27`; metal avg `-0.6416` n `20`; unknown avg `11.639` n `869`
- 24h: commodity avg `-0.6621` n `12`; crypto_alt avg `-1.2562` n `234`; crypto_major avg `0.017` n `8`; equity avg `0.1122` n `137`; fx avg `0.0547` n `6`; index avg `-0.0436` n `27`; metal avg `-0.363` n `20`; unknown avg `4.38` n `799`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
