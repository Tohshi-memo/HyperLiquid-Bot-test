# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T22:22:13.403009+00:00`
- Correlation status: `ready`
- Asset price records: `589`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.3305` n `12`; crypto_alt avg `0.4504` n `228`; crypto_major avg `0.2781` n `8`; equity avg `0.1485` n `65`; fx avg `0.0137` n `5`; index avg `0.1255` n `23`; metal avg `0.2873` n `18`; unknown avg `0.0831` n `365`
- 1h: commodity avg `-0.7502` n `12`; crypto_alt avg `0.3353` n `228`; crypto_major avg `-0.0198` n `8`; equity avg `-0.364` n `65`; fx avg `0.0077` n `5`; index avg `0.0152` n `23`; metal avg `0.1945` n `18`; unknown avg `-0.044` n `365`
- 4h: commodity avg `0.5995` n `12`; crypto_alt avg `-0.0597` n `228`; crypto_major avg `-0.4497` n `8`; equity avg `-0.5432` n `65`; fx avg `-0.0006` n `5`; index avg `-0.1126` n `23`; metal avg `-0.5497` n `18`; unknown avg `-0.6114` n `365`
- 24h: commodity avg `0.6442` n `12`; crypto_alt avg `1.3322` n `228`; crypto_major avg `-1.8237` n `8`; equity avg `-1.4642` n `65`; fx avg `0.1715` n `5`; index avg `-0.787` n `23`; metal avg `-0.2415` n `18`; unknown avg `-0.7176` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1398`, n `585`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `585`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `585`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `585`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `581`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `581`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.092`, n `581`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0884`, n `581`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0829`, n `581`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `581`, weak_sample_signal
