# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T17:37:12.617110+00:00`
- Correlation status: `ready`
- Asset price records: `570`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.4434` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.3227` n `12`; crypto_alt avg `-0.0424` n `228`; crypto_major avg `0.0205` n `8`; equity avg `0.0292` n `65`; fx avg `-0.0219` n `5`; index avg `0.0253` n `23`; metal avg `-0.0876` n `18`; unknown avg `0.2686` n `365`
- 1h: commodity avg `0.5441` n `12`; crypto_alt avg `0.1598` n `228`; crypto_major avg `-0.0189` n `8`; equity avg `-0.3612` n `65`; fx avg `-0.0099` n `5`; index avg `-0.302` n `23`; metal avg `-0.3867` n `18`; unknown avg `0.0971` n `365`
- 4h: commodity avg `2.3312` n `12`; crypto_alt avg `-0.64` n `228`; crypto_major avg `-1.1122` n `8`; equity avg `-1.6586` n `65`; fx avg `0.0446` n `5`; index avg `-0.7452` n `23`; metal avg `-1.3912` n `18`; unknown avg `-0.3572` n `365`
- 24h: commodity avg `0.6724` n `12`; crypto_alt avg `0.5243` n `228`; crypto_major avg `-1.9598` n `8`; equity avg `-0.8715` n `65`; fx avg `0.1801` n `5`; index avg `-0.5445` n `23`; metal avg `0.6195` n `18`; unknown avg `-0.0094` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1361`, n `566`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1156`, n `566`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `566`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `566`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1007`, n `562`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0953`, n `562`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `562`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `562`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0872`, n `562`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `566`, weak_sample_signal
