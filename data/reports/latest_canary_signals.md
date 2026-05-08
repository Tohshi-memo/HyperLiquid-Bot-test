# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T07:22:21.238891+00:00`
- Correlation status: `ready`
- Asset price records: `625`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1454` n `12`; crypto_alt avg `0.1495` n `228`; crypto_major avg `0.086` n `8`; equity avg `-0.0112` n `65`; fx avg `0.0075` n `5`; index avg `0.004` n `23`; metal avg `-0.3164` n `18`; unknown avg `-0.0796` n `375`
- 1h: commodity avg `0.1413` n `12`; crypto_alt avg `-0.1644` n `228`; crypto_major avg `-0.0736` n `8`; equity avg `0.0321` n `65`; fx avg `-0.0033` n `5`; index avg `-0.0097` n `23`; metal avg `-0.4314` n `18`; unknown avg `0.1781` n `375`
- 4h: commodity avg `-0.106` n `12`; crypto_alt avg `-0.1079` n `228`; crypto_major avg `-0.2912` n `8`; equity avg `0.5105` n `65`; fx avg `0.1177` n `5`; index avg `0.1597` n `23`; metal avg `0.1644` n `18`; unknown avg `-0.0457` n `355`
- 24h: commodity avg `1.502` n `12`; crypto_alt avg `0.2804` n `228`; crypto_major avg `-2.327` n `8`; equity avg `-1.2937` n `65`; fx avg `0.3281` n `5`; index avg `-0.696` n `23`; metal avg `-0.4863` n `18`; unknown avg `-0.7376` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1342`, n `617`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1334`, n `617`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `621`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1158`, n `621`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1126`, n `621`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `621`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0846`, n `617`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0816`, n `617`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.081`, n `617`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0659`, n `621`, weak_sample_signal
