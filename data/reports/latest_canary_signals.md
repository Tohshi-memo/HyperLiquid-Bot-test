# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T23:12:51.305674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8937` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.761` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0964` n `13`; crypto_alt avg `0.7477` n `239`; crypto_major avg `0.9093` n `8`; equity avg `0.4231` n `158`; fx avg `0.0107` n `6`; index avg `0.1068` n `27`; metal avg `0.1611` n `20`; unknown avg `1.7193` n `1246`
- 1h: commodity avg `-0.0848` n `13`; crypto_alt avg `1.1755` n `239`; crypto_major avg `1.0679` n `8`; equity avg `0.4223` n `158`; fx avg `0.0227` n `6`; index avg `0.0769` n `27`; metal avg `0.1753` n `20`; unknown avg `1.647` n `1228`
- 4h: commodity avg `0.0745` n `13`; crypto_alt avg `-1.5265` n `239`; crypto_major avg `-1.8269` n `8`; equity avg `-0.7974` n `158`; fx avg `-0.0239` n `6`; index avg `-0.0659` n `27`; metal avg `0.0668` n `20`; unknown avg `1.1956` n `1172`
- 24h: commodity avg `-0.0779` n `13`; crypto_alt avg `-2.7265` n `239`; crypto_major avg `-1.9145` n `8`; equity avg `-0.3553` n `158`; fx avg `0.0424` n `6`; index avg `-0.0431` n `27`; metal avg `0.0448` n `20`; unknown avg `-0.1597` n `1002`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
