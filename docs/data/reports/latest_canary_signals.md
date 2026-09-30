# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T10:07:36.318394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `-0.0335` n `234`; crypto_major avg `0.1173` n `8`; equity avg `-0.0133` n `142`; fx avg `0.0075` n `6`; index avg `-0.0062` n `26`; metal avg `0.0091` n `20`; unknown avg `5.6087` n `961`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `0.24` n `234`; crypto_major avg `0.5178` n `8`; equity avg `-0.0277` n `142`; fx avg `0.0309` n `6`; index avg `-0.0234` n `26`; metal avg `-0.0565` n `20`; unknown avg `2.3678` n `961`
- 4h: commodity avg `0.1784` n `12`; crypto_alt avg `0.578` n `234`; crypto_major avg `0.4619` n `8`; equity avg `0.0264` n `142`; fx avg `0.0436` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0184` n `20`; unknown avg `2.3511` n `941`
- 24h: commodity avg `-0.3437` n `12`; crypto_alt avg `0.0995` n `234`; crypto_major avg `-0.5946` n `8`; equity avg `0.1371` n `142`; fx avg `-0.0011` n `6`; index avg `0.0491` n `26`; metal avg `0.1219` n `20`; unknown avg `2922.5346` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
