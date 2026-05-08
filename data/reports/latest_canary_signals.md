# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T17:52:17.422315+00:00`
- Correlation status: `ready`
- Asset price records: `667`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8618` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `0.0387` n `228`; crypto_major avg `0.1031` n `8`; equity avg `-0.1316` n `65`; fx avg `0.0002` n `5`; index avg `-0.0701` n `23`; metal avg `-0.0276` n `18`; unknown avg `-0.2269` n `375`
- 1h: commodity avg `-0.1635` n `12`; crypto_alt avg `0.7792` n `228`; crypto_major avg `0.8869` n `8`; equity avg `0.3144` n `65`; fx avg `0.0052` n `5`; index avg `0.1818` n `23`; metal avg `0.1894` n `18`; unknown avg `-0.0213` n `375`
- 4h: commodity avg `0.3854` n `12`; crypto_alt avg `2.1452` n `228`; crypto_major avg `1.4782` n `8`; equity avg `0.7172` n `65`; fx avg `-0.0005` n `5`; index avg `0.2344` n `23`; metal avg `-0.3836` n `18`; unknown avg `-0.1569` n `375`
- 24h: commodity avg `0.0779` n `12`; crypto_alt avg `3.4305` n `228`; crypto_major avg `1.2066` n `8`; equity avg `2.7695` n `65`; fx avg `0.1483` n `5`; index avg `1.5395` n `23`; metal avg `0.6581` n `18`; unknown avg `0.3266` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.121`, n `659`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1166`, n `659`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `663`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `659`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `663`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0955`, n `659`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `663`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `663`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `663`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `663`, weak_sample_signal
