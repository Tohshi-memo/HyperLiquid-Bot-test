# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T21:07:18.378200+00:00`
- Correlation status: `ready`
- Asset price records: `584`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.467` n `12`; crypto_alt avg `-0.4026` n `228`; crypto_major avg `-0.2505` n `8`; equity avg `-0.1849` n `65`; fx avg `-0.0398` n `5`; index avg `0.0314` n `23`; metal avg `-0.4158` n `18`; unknown avg `-0.1007` n `365`
- 1h: commodity avg `1.2182` n `12`; crypto_alt avg `-0.9427` n `228`; crypto_major avg `-0.4929` n `8`; equity avg `-0.6486` n `65`; fx avg `-0.0431` n `5`; index avg `-0.0212` n `23`; metal avg `-0.762` n `18`; unknown avg `-0.2895` n `365`
- 4h: commodity avg `0.9582` n `12`; crypto_alt avg `0.1543` n `228`; crypto_major avg `-0.2246` n `8`; equity avg `-0.0615` n `65`; fx avg `-0.0633` n `5`; index avg `-0.0919` n `23`; metal avg `-0.9663` n `18`; unknown avg `-0.5655` n `365`
- 24h: commodity avg `1.0896` n `12`; crypto_alt avg `0.6239` n `228`; crypto_major avg `-2.1104` n `8`; equity avg `-1.2337` n `65`; fx avg `0.1532` n `5`; index avg `-0.8171` n `23`; metal avg `-0.3346` n `18`; unknown avg `-0.5446` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1399`, n `580`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.116`, n `580`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `580`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `580`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `576`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `576`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0892`, n `576`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0849`, n `576`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.083`, n `576`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0786`, n `576`, weak_sample_signal
