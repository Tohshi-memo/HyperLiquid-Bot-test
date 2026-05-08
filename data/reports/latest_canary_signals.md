# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T07:52:15.440794+00:00`
- Correlation status: `ready`
- Asset price records: `627`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0321` n `12`; crypto_alt avg `0.1292` n `228`; crypto_major avg `0.1155` n `8`; equity avg `0.1309` n `65`; fx avg `-0.0048` n `5`; index avg `0.0044` n `23`; metal avg `0.0042` n `18`; unknown avg `0.3235` n `375`
- 1h: commodity avg `0.0829` n `12`; crypto_alt avg `0.1248` n `228`; crypto_major avg `0.1964` n `8`; equity avg `0.1895` n `65`; fx avg `-0.0041` n `5`; index avg `-0.0505` n `23`; metal avg `-0.4321` n `18`; unknown avg `0.3399` n `375`
- 4h: commodity avg `-0.0542` n `12`; crypto_alt avg `-0.1385` n `228`; crypto_major avg `-0.0178` n `8`; equity avg `0.6525` n `65`; fx avg `0.0784` n `5`; index avg `0.1114` n `23`; metal avg `0.0508` n `18`; unknown avg `0.3289` n `355`
- 24h: commodity avg `1.0756` n `12`; crypto_alt avg `0.3578` n `228`; crypto_major avg `-2.3494` n `8`; equity avg `-1.0504` n `65`; fx avg `0.2959` n `5`; index avg `-0.7528` n `23`; metal avg `-0.6888` n `18`; unknown avg `-0.0115` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1318`, n `619`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1313`, n `619`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `623`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.114`, n `623`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `623`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `623`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `619`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `619`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0803`, n `619`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0663`, n `623`, weak_sample_signal
