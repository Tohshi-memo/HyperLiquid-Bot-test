# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T13:37:19.379443+00:00`
- Correlation status: `ready`
- Asset price records: `650`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0899` n `12`; crypto_alt avg `-0.0398` n `228`; crypto_major avg `0.0295` n `8`; equity avg `0.3999` n `65`; fx avg `-0.011` n `5`; index avg `0.0484` n `23`; metal avg `0.3311` n `18`; unknown avg `0.1885` n `375`
- 1h: commodity avg `-0.0605` n `12`; crypto_alt avg `-0.2249` n `228`; crypto_major avg `-0.3511` n `8`; equity avg `0.3145` n `65`; fx avg `-0.0333` n `5`; index avg `-0.0126` n `23`; metal avg `0.007` n `18`; unknown avg `0.09` n `375`
- 4h: commodity avg `0.0699` n `12`; crypto_alt avg `-0.1938` n `228`; crypto_major avg `-0.2261` n `8`; equity avg `0.4809` n `65`; fx avg `-0.035` n `5`; index avg `0.2067` n `23`; metal avg `0.2802` n `18`; unknown avg `0.0438` n `375`
- 24h: commodity avg `1.9265` n `12`; crypto_alt avg `0.5551` n `228`; crypto_major avg `-1.3239` n `8`; equity avg `0.1236` n `65`; fx avg `0.2017` n `5`; index avg `0.0442` n `23`; metal avg `-0.468` n `18`; unknown avg `-0.5785` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1253`, n `642`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1225`, n `642`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `646`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `646`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `646`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0907`, n `642`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.09`, n `646`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `642`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `646`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.067`, n `646`, weak_sample_signal
