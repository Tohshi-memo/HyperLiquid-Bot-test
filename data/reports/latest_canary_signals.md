# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T05:22:34.190224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1049` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.7353` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7053` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0432` n `13`; crypto_alt avg `-0.1503` n `234`; crypto_major avg `-0.1671` n `8`; equity avg `-0.0239` n `142`; fx avg `-0.0251` n `6`; index avg `0.0013` n `26`; metal avg `0.0016` n `20`; unknown avg `-0.1604` n `985`
- 1h: commodity avg `-0.0001` n `13`; crypto_alt avg `0.5716` n `234`; crypto_major avg `0.3834` n `8`; equity avg `0.0876` n `142`; fx avg `-0.0456` n `6`; index avg `0.0113` n `26`; metal avg `0.026` n `20`; unknown avg `-0.4532` n `981`
- 4h: commodity avg `-0.0669` n `13`; crypto_alt avg `1.9615` n `234`; crypto_major avg `2.038` n `8`; equity avg `0.3027` n `142`; fx avg `-0.096` n `6`; index avg `0.0771` n `26`; metal avg `0.3327` n `20`; unknown avg `5.228` n `975`
- 24h: commodity avg `0.282` n `13`; crypto_alt avg `0.1983` n `234`; crypto_major avg `1.1296` n `8`; equity avg `0.2022` n `142`; fx avg `-0.2478` n `6`; index avg `-0.0365` n `26`; metal avg `-0.1078` n `20`; unknown avg `0.0956` n `838`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
