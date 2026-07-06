# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T18:22:27.198774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.3381` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.165` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9261` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `0.0816` n `229`; crypto_major avg `0.0425` n `8`; equity avg `0.1504` n `91`; fx avg `-0.0031` n `6`; index avg `0.0152` n `25`; metal avg `0.0679` n `20`; unknown avg `0.0489` n `763`
- 1h: commodity avg `0.0876` n `12`; crypto_alt avg `-0.0023` n `229`; crypto_major avg `-0.1874` n `8`; equity avg `-0.256` n `91`; fx avg `-0.0145` n `6`; index avg `-0.01` n `25`; metal avg `0.1397` n `20`; unknown avg `0.0107` n `763`
- 4h: commodity avg `-0.04` n `12`; crypto_alt avg `2.0392` n `229`; crypto_major avg `2.125` n `8`; equity avg `-0.2131` n `90`; fx avg `0.0181` n `6`; index avg `-0.0195` n `25`; metal avg `0.1989` n `20`; unknown avg `2.5893` n `763`
- 24h: commodity avg `-0.0668` n `12`; crypto_alt avg `0.9818` n `229`; crypto_major avg `0.7715` n `8`; equity avg `-0.5269` n `90`; fx avg `0.1946` n `6`; index avg `0.0294` n `25`; metal avg `-0.1685` n `20`; unknown avg `0.7195` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
