# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T19:22:24.271220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5452` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0106` n `13`; crypto_alt avg `0.1758` n `239`; crypto_major avg `0.2194` n `8`; equity avg `0.0789` n `168`; fx avg `-0.0034` n `6`; index avg `0.0101` n `27`; metal avg `-0.02` n `20`; unknown avg `-0.0596` n `1261`
- 1h: commodity avg `0.0157` n `13`; crypto_alt avg `0.4598` n `239`; crypto_major avg `0.6046` n `8`; equity avg `0.2913` n `168`; fx avg `-0.0058` n `6`; index avg `0.0255` n `27`; metal avg `-0.011` n `20`; unknown avg `32.9449` n `1245`
- 4h: commodity avg `0.0117` n `13`; crypto_alt avg `1.359` n `239`; crypto_major avg `1.4613` n `8`; equity avg `0.2984` n `168`; fx avg `-0.0128` n `6`; index avg `0.0229` n `27`; metal avg `-0.0839` n `20`; unknown avg `33.3359` n `1199`
- 24h: commodity avg `0.1387` n `13`; crypto_alt avg `1.4698` n `239`; crypto_major avg `0.592` n `8`; equity avg `1.1257` n `168`; fx avg `-0.0376` n `6`; index avg `0.0794` n `27`; metal avg `0.2449` n `20`; unknown avg `30.8779` n `1031`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
