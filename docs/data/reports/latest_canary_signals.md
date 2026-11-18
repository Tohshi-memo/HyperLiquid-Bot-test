# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T00:07:43.062736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7596` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6386` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0068` n `13`; crypto_alt avg `-0.0391` n `239`; crypto_major avg `-0.0231` n `8`; equity avg `0.1706` n `163`; fx avg `-0.046` n `6`; index avg `0.0224` n `27`; metal avg `-0.0729` n `20`; unknown avg `1.1676` n `1254`
- 1h: commodity avg `0.0468` n `13`; crypto_alt avg `0.1047` n `239`; crypto_major avg `0.0454` n `8`; equity avg `-0.0419` n `163`; fx avg `-0.0646` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0978` n `20`; unknown avg `1.2623` n `1257`
- 4h: commodity avg `0.1658` n `13`; crypto_alt avg `1.7204` n `239`; crypto_major avg `1.8338` n `8`; equity avg `3.4724` n `163`; fx avg `-0.0733` n `6`; index avg `0.3416` n `27`; metal avg `0.0742` n `20`; unknown avg `3.5675` n `1195`
- 24h: commodity avg `0.3255` n `13`; crypto_alt avg `1.4326` n `239`; crypto_major avg `1.6325` n `8`; equity avg `1.8239` n `163`; fx avg `-0.0525` n `6`; index avg `0.173` n `27`; metal avg `-0.0559` n `20`; unknown avg `7.9129` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
