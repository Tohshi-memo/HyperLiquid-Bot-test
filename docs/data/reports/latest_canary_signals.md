# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T21:37:29.405786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6517` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `-0.047` n `234`; crypto_major avg `-0.1139` n `8`; equity avg `0.1157` n `137`; fx avg `-0.0168` n `6`; index avg `-0.0` n `27`; metal avg `0.0027` n `20`; unknown avg `1.087` n `919`
- 1h: commodity avg `0.0496` n `12`; crypto_alt avg `0.236` n `234`; crypto_major avg `-0.2185` n `8`; equity avg `0.2362` n `137`; fx avg `-0.0353` n `6`; index avg `0.0123` n `27`; metal avg `0.0168` n `20`; unknown avg `5.8755` n `917`
- 4h: commodity avg `0.0344` n `12`; crypto_alt avg `1.6974` n `234`; crypto_major avg `1.1653` n `8`; equity avg `-0.2285` n `137`; fx avg `0.0396` n `6`; index avg `-0.1779` n `27`; metal avg `-0.4864` n `20`; unknown avg `5.3323` n `829`
- 24h: commodity avg `-0.5796` n `12`; crypto_alt avg `0.3625` n `234`; crypto_major avg `0.7923` n `8`; equity avg `1.016` n `137`; fx avg `0.0749` n `6`; index avg `0.0306` n `27`; metal avg `-0.2636` n `20`; unknown avg `4.7142` n `771`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
