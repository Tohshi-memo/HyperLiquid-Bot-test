# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T03:07:29.138495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8217` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7984` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.3191` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0024` n `13`; crypto_alt avg `-0.7211` n `239`; crypto_major avg `-0.804` n `8`; equity avg `-0.1415` n `166`; fx avg `-0.0001` n `6`; index avg `-0.0114` n `27`; metal avg `-0.0362` n `20`; unknown avg `0.093` n `1252`
- 1h: commodity avg `0.0255` n `13`; crypto_alt avg `-0.991` n `239`; crypto_major avg `-1.3389` n `8`; equity avg `-0.2774` n `166`; fx avg `-0.0033` n `6`; index avg `-0.0198` n `27`; metal avg `-0.0257` n `20`; unknown avg `0.2183` n `1256`
- 4h: commodity avg `-0.012` n `13`; crypto_alt avg `-1.7942` n `239`; crypto_major avg `-1.8507` n `8`; equity avg `-0.4816` n `166`; fx avg `-0.0101` n `6`; index avg `-0.029` n `27`; metal avg `-0.0523` n `20`; unknown avg `2.8095` n `1248`
- 24h: commodity avg `0.3421` n `13`; crypto_alt avg `-4.8242` n `239`; crypto_major avg `-6.3134` n `8`; equity avg `-4.9324` n `166`; fx avg `-0.0397` n `6`; index avg `-0.537` n `27`; metal avg `0.0048` n `20`; unknown avg `12.5505` n `1115`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
