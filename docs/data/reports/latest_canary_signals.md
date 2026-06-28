# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T09:47:53.767471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `-0.1269` n `228`; crypto_major avg `-0.0274` n `8`; equity avg `-0.0136` n `88`; fx avg `-0.0021` n `6`; index avg `0.0006` n `23`; metal avg `-0.0117` n `20`; unknown avg `2.1278` n `750`
- 1h: commodity avg `0.0172` n `12`; crypto_alt avg `-0.2019` n `228`; crypto_major avg `-0.2153` n `8`; equity avg `0.0108` n `88`; fx avg `0.0155` n `6`; index avg `-0.0049` n `23`; metal avg `-0.0075` n `20`; unknown avg `-0.5112` n `750`
- 4h: commodity avg `0.0472` n `12`; crypto_alt avg `0.3767` n `228`; crypto_major avg `0.7469` n `8`; equity avg `0.3042` n `88`; fx avg `0.0222` n `6`; index avg `0.0546` n `23`; metal avg `0.0196` n `20`; unknown avg `-0.1524` n `724`
- 24h: commodity avg `0.1942` n `12`; crypto_alt avg `0.0224` n `228`; crypto_major avg `-0.4409` n `8`; equity avg `0.1437` n `88`; fx avg `0.0023` n `6`; index avg `-0.055` n `23`; metal avg `-0.0138` n `20`; unknown avg `16.421` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2187`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
