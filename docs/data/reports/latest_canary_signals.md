# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T01:52:26.877963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `13`; crypto_alt avg `-0.1305` n `239`; crypto_major avg `-0.0439` n `8`; equity avg `-0.2055` n `168`; fx avg `0.0031` n `6`; index avg `-0.0159` n `27`; metal avg `0.1679` n `20`; unknown avg `0.201` n `1263`
- 1h: commodity avg `0.0396` n `13`; crypto_alt avg `0.0038` n `239`; crypto_major avg `0.0412` n `8`; equity avg `0.8982` n `168`; fx avg `0.0074` n `6`; index avg `0.1137` n `27`; metal avg `0.3841` n `20`; unknown avg `0.8401` n `1257`
- 4h: commodity avg `0.1379` n `13`; crypto_alt avg `-0.214` n `239`; crypto_major avg `-0.3898` n `8`; equity avg `0.5294` n `168`; fx avg `-0.0062` n `6`; index avg `0.0882` n `27`; metal avg `0.2629` n `20`; unknown avg `2.4173` n `1205`
- 24h: commodity avg `0.2239` n `13`; crypto_alt avg `0.4694` n `239`; crypto_major avg `0.187` n `8`; equity avg `0.8011` n `168`; fx avg `0.0186` n `6`; index avg `0.0871` n `27`; metal avg `0.4603` n `20`; unknown avg `181.9879` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
