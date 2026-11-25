# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T17:37:33.467475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9001` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0207` n `13`; crypto_alt avg `0.1979` n `239`; crypto_major avg `0.3068` n `8`; equity avg `0.3499` n `168`; fx avg `-0.0073` n `6`; index avg `0.0487` n `27`; metal avg `-0.047` n `20`; unknown avg `0.4544` n `1266`
- 1h: commodity avg `0.2089` n `13`; crypto_alt avg `2.2242` n `239`; crypto_major avg `1.9528` n `8`; equity avg `2.7207` n `168`; fx avg `0.0454` n `6`; index avg `0.3125` n `27`; metal avg `0.5613` n `20`; unknown avg `8.8016` n `1264`
- 4h: commodity avg `0.4357` n `13`; crypto_alt avg `2.0111` n `239`; crypto_major avg `1.9917` n `8`; equity avg `0.8406` n `168`; fx avg `0.0746` n `6`; index avg `0.1465` n `27`; metal avg `0.0916` n `20`; unknown avg `202.8607` n `1239`
- 24h: commodity avg `0.3999` n `13`; crypto_alt avg `0.0523` n `239`; crypto_major avg `-0.9583` n `8`; equity avg `-3.389` n `168`; fx avg `-0.016` n `6`; index avg `-0.3439` n `27`; metal avg `-0.5576` n `20`; unknown avg `638.9683` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
