# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T21:22:26.222423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.503` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `0.0073` n `234`; crypto_major avg `-0.1546` n `8`; equity avg `0.0177` n `137`; fx avg `0.0051` n `6`; index avg `0.0003` n `27`; metal avg `-0.0053` n `20`; unknown avg `2.4119` n `919`
- 1h: commodity avg `0.0216` n `12`; crypto_alt avg `0.1166` n `234`; crypto_major avg `-0.4697` n `8`; equity avg `0.0588` n `137`; fx avg `-0.0212` n `6`; index avg `0.0119` n `27`; metal avg `0.0284` n `20`; unknown avg `1.4215` n `911`
- 4h: commodity avg `-0.018` n `12`; crypto_alt avg `1.5117` n `234`; crypto_major avg `1.0282` n `8`; equity avg `-0.3675` n `137`; fx avg `0.0571` n `6`; index avg `-0.1775` n `27`; metal avg `-0.4748` n `20`; unknown avg `4.5299` n `829`
- 24h: commodity avg `-0.5911` n `12`; crypto_alt avg `0.2299` n `234`; crypto_major avg `0.8057` n `8`; equity avg `0.8615` n `137`; fx avg `0.0897` n `6`; index avg `0.027` n `27`; metal avg `-0.271` n `20`; unknown avg `4.5043` n `771`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
