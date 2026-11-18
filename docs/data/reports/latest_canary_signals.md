# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T00:52:25.530870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.9397` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5252` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0119` n `13`; crypto_alt avg `-0.1238` n `239`; crypto_major avg `-0.2192` n `8`; equity avg `0.1917` n `163`; fx avg `0.0021` n `6`; index avg `0.01` n `27`; metal avg `-0.05` n `20`; unknown avg `2.9576` n `1266`
- 1h: commodity avg `-0.0539` n `13`; crypto_alt avg `-0.4317` n `239`; crypto_major avg `-0.296` n `8`; equity avg `0.2146` n `163`; fx avg `-0.0537` n `6`; index avg `0.0109` n `27`; metal avg `-0.2793` n `20`; unknown avg `3.2827` n `1258`
- 4h: commodity avg `0.0492` n `13`; crypto_alt avg `1.0222` n `239`; crypto_major avg `1.403` n `8`; equity avg `3.3427` n `163`; fx avg `-0.0789` n `6`; index avg `0.321` n `27`; metal avg `-0.1222` n `20`; unknown avg `3.6728` n `1195`
- 24h: commodity avg `0.2912` n `13`; crypto_alt avg `1.3697` n `239`; crypto_major avg `1.5381` n `8`; equity avg `1.9209` n `163`; fx avg `-0.0668` n `6`; index avg `0.1383` n `27`; metal avg `-0.2253` n `20`; unknown avg `7.6704` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
