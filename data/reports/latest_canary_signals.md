# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T13:52:20.117320+00:00`
- Correlation status: `ready`
- Asset price records: `555`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.303` n `12`; crypto_alt avg `-0.4556` n `228`; crypto_major avg `-0.4276` n `8`; equity avg `-0.4722` n `65`; fx avg `0.0028` n `5`; index avg `-0.2166` n `23`; metal avg `-0.2697` n `18`; unknown avg `-0.1467` n `365`
- 1h: commodity avg `0.6126` n `12`; crypto_alt avg `-0.8441` n `228`; crypto_major avg `-0.941` n `8`; equity avg `-0.5078` n `65`; fx avg `0.0253` n `5`; index avg `-0.4075` n `23`; metal avg `-0.5355` n `18`; unknown avg `0.5623` n `365`
- 4h: commodity avg `-0.4831` n `12`; crypto_alt avg `-0.0493` n `228`; crypto_major avg `-0.6977` n `8`; equity avg `-0.7976` n `65`; fx avg `-0.009` n `5`; index avg `-0.4483` n `23`; metal avg `-0.0401` n `18`; unknown avg `0.8246` n `357`
- 24h: commodity avg `-1.4031` n `12`; crypto_alt avg `1.0016` n `228`; crypto_major avg `-1.4737` n `8`; equity avg `1.2127` n `65`; fx avg `0.1249` n `5`; index avg `0.4408` n `23`; metal avg `1.7578` n `18`; unknown avg `1.3803` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1352`, n `551`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1247`, n `551`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0966`, n `551`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0827`, n `547`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0785`, n `547`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `547`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `551`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `547`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `551`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0668`, n `547`, weak_sample_signal
