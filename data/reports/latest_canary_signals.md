# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T05:07:34.617033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6092` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5861` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0456` n `13`; crypto_alt avg `-0.1433` n `234`; crypto_major avg `-0.2032` n `8`; equity avg `0.0115` n `142`; fx avg `0.0031` n `6`; index avg `0.0058` n `26`; metal avg `0.0509` n `20`; unknown avg `0.2785` n `981`
- 1h: commodity avg `-0.044` n `13`; crypto_alt avg `1.1636` n `234`; crypto_major avg `0.9999` n `8`; equity avg `0.1522` n `142`; fx avg `-0.0218` n `6`; index avg `0.0106` n `26`; metal avg `0.0476` n `20`; unknown avg `1.9976` n `981`
- 4h: commodity avg `-0.0867` n `13`; crypto_alt avg `1.8044` n `234`; crypto_major avg `1.885` n `8`; equity avg `0.2758` n `142`; fx avg `-0.0697` n `6`; index avg `0.063` n `26`; metal avg `0.2989` n `20`; unknown avg `2.8413` n `975`
- 24h: commodity avg `0.6307` n `13`; crypto_alt avg `0.4332` n `234`; crypto_major avg `1.3884` n `8`; equity avg `0.2758` n `142`; fx avg `-0.2136` n `6`; index avg `-0.025` n `26`; metal avg `-0.1012` n `20`; unknown avg `0.761` n `838`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
