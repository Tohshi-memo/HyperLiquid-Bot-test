# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T13:22:29.614886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0455` n `12`; crypto_alt avg `0.2061` n `234`; crypto_major avg `0.2923` n `8`; equity avg `0.1203` n `140`; fx avg `0.0058` n `6`; index avg `0.0097` n `26`; metal avg `-0.0058` n `20`; unknown avg `0.8794` n `928`
- 1h: commodity avg `0.1184` n `12`; crypto_alt avg `0.3479` n `234`; crypto_major avg `0.2945` n `8`; equity avg `0.1138` n `140`; fx avg `-0.008` n `6`; index avg `0.012` n `26`; metal avg `0.01` n `20`; unknown avg `0.1631` n `920`
- 4h: commodity avg `0.3942` n `12`; crypto_alt avg `0.0895` n `234`; crypto_major avg `0.0268` n `8`; equity avg `-0.5409` n `140`; fx avg `-0.002` n `6`; index avg `-0.1047` n `26`; metal avg `-0.2076` n `20`; unknown avg `1.1509` n `917`
- 24h: commodity avg `0.327` n `12`; crypto_alt avg `5.3305` n `234`; crypto_major avg `3.7234` n `8`; equity avg `0.6577` n `140`; fx avg `0.2334` n `6`; index avg `-0.0348` n `26`; metal avg `0.1575` n `20`; unknown avg `1.7345` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
