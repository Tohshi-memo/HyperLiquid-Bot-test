# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T08:22:16.818152+00:00`
- Correlation status: `ready`
- Asset price records: `629`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0661` n `12`; crypto_alt avg `-0.113` n `228`; crypto_major avg `-0.0522` n `8`; equity avg `0.0749` n `65`; fx avg `-0.0115` n `5`; index avg `0.0236` n `23`; metal avg `0.2596` n `18`; unknown avg `-0.0173` n `375`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `0.3812` n `228`; crypto_major avg `0.4042` n `8`; equity avg `0.5442` n `65`; fx avg `-0.0057` n `5`; index avg `0.1131` n `23`; metal avg `0.2984` n `18`; unknown avg `0.3594` n `375`
- 4h: commodity avg `-0.2674` n `12`; crypto_alt avg `-0.118` n `228`; crypto_major avg `0.0099` n `8`; equity avg `0.8141` n `65`; fx avg `0.0639` n `5`; index avg `0.2159` n `23`; metal avg `0.3707` n `18`; unknown avg `0.3431` n `355`
- 24h: commodity avg `0.8911` n `12`; crypto_alt avg `0.5783` n `228`; crypto_major avg `-1.951` n `8`; equity avg `-0.5694` n `65`; fx avg `0.2533` n `5`; index avg `-0.6191` n `23`; metal avg `-0.3613` n `18`; unknown avg `-0.1193` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1316`, n `621`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1314`, n `621`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `625`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `625`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1045`, n `625`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `625`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `621`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `621`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `621`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `625`, weak_sample_signal
