# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T16:31:00.588680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.009` n `229`; crypto_major avg `0.0525` n `8`; equity avg `-0.0182` n `88`; fx avg `-0.0007` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.0177` n `765`
- 1h: commodity avg `0.0285` n `12`; crypto_alt avg `0.2632` n `229`; crypto_major avg `0.025` n `8`; equity avg `-0.0024` n `88`; fx avg `-0.0049` n `6`; index avg `-0.0042` n `25`; metal avg `0.0081` n `20`; unknown avg `0.179` n `765`
- 4h: commodity avg `-0.045` n `12`; crypto_alt avg `0.8675` n `229`; crypto_major avg `0.9601` n `8`; equity avg `0.0418` n `88`; fx avg `0.0184` n `6`; index avg `-0.0133` n `25`; metal avg `0.0345` n `20`; unknown avg `0.3154` n `759`
- 24h: commodity avg `0.0415` n `12`; crypto_alt avg `1.5351` n `229`; crypto_major avg `2.0475` n `8`; equity avg `0.2511` n `88`; fx avg `-0.0222` n `6`; index avg `-0.049` n `25`; metal avg `0.0745` n `20`; unknown avg `1.8634` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
