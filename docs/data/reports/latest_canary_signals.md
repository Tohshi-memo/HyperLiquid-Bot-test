# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T06:22:26.529911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `13`; crypto_alt avg `0.0897` n `239`; crypto_major avg `0.173` n `8`; equity avg `0.0161` n `162`; fx avg `0.0015` n `6`; index avg `0.0011` n `27`; metal avg `0.024` n `20`; unknown avg `158.8515` n `1261`
- 1h: commodity avg `0.0087` n `13`; crypto_alt avg `-0.5273` n `239`; crypto_major avg `-0.8853` n `8`; equity avg `-0.2162` n `162`; fx avg `0.0027` n `6`; index avg `-0.0165` n `27`; metal avg `-0.0264` n `20`; unknown avg `2.1062` n `1245`
- 4h: commodity avg `0.0195` n `13`; crypto_alt avg `0.1271` n `239`; crypto_major avg `0.0621` n `8`; equity avg `0.009` n `162`; fx avg `0.0148` n `6`; index avg `-0.014` n `27`; metal avg `-0.0013` n `20`; unknown avg `1.9902` n `1229`
- 24h: commodity avg `0.068` n `13`; crypto_alt avg `-6.1101` n `239`; crypto_major avg `-5.1652` n `8`; equity avg `-1.0882` n `162`; fx avg `0.0471` n `6`; index avg `-0.1055` n `27`; metal avg `-0.4832` n `20`; unknown avg `48.5427` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
