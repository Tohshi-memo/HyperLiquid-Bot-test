# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T14:52:17.320036+00:00`
- Correlation status: `ready`
- Asset price records: `559`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1586` n `12`; crypto_alt avg `0.3436` n `228`; crypto_major avg `0.1804` n `8`; equity avg `0.003` n `65`; fx avg `0.0102` n `5`; index avg `0.0166` n `23`; metal avg `0.1738` n `18`; unknown avg `0.0025` n `365`
- 1h: commodity avg `0.0991` n `12`; crypto_alt avg `-0.3287` n `228`; crypto_major avg `-0.3335` n `8`; equity avg `0.3494` n `65`; fx avg `-0.0126` n `5`; index avg `0.2414` n `23`; metal avg `0.4614` n `18`; unknown avg `-0.2847` n `365`
- 4h: commodity avg `-0.4918` n `12`; crypto_alt avg `-0.457` n `228`; crypto_major avg `-0.9165` n `8`; equity avg `-0.2044` n `65`; fx avg `-0.0245` n `5`; index avg `-0.2591` n `23`; metal avg `0.4378` n `18`; unknown avg `-0.0939` n `365`
- 24h: commodity avg `-1.1373` n `12`; crypto_alt avg `0.6648` n `228`; crypto_major avg `-1.7455` n `8`; equity avg `1.0708` n `65`; fx avg `0.1102` n `5`; index avg `0.4056` n `23`; metal avg `1.8928` n `18`; unknown avg `0.0664` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.134`, n `555`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.124`, n `555`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `555`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0966`, n `555`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `555`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `551`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0784`, n `551`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `551`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `555`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0752`, n `551`, weak_sample_signal
