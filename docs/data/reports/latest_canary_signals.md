# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T12:07:46.851266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3149` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0308` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0722` n `12`; crypto_alt avg `0.1091` n `229`; crypto_major avg `0.0263` n `8`; equity avg `0.2454` n `88`; fx avg `0.0044` n `6`; index avg `0.0351` n `25`; metal avg `0.0147` n `20`; unknown avg `-0.086` n `763`
- 1h: commodity avg `-0.0388` n `12`; crypto_alt avg `0.2253` n `229`; crypto_major avg `0.4034` n `8`; equity avg `0.4778` n `88`; fx avg `-0.0222` n `6`; index avg `0.0915` n `25`; metal avg `0.1262` n `20`; unknown avg `-0.3641` n `763`
- 4h: commodity avg `-0.1449` n `12`; crypto_alt avg `1.2349` n `228`; crypto_major avg `2.17` n `8`; equity avg `1.0412` n `88`; fx avg `-0.0325` n `6`; index avg `0.1446` n `25`; metal avg `0.1392` n `20`; unknown avg `-0.1386` n `763`
- 24h: commodity avg `-0.5386` n `12`; crypto_alt avg `3.4256` n `228`; crypto_major avg `4.678` n `8`; equity avg `-1.2824` n `88`; fx avg `-0.1089` n `6`; index avg `-0.4484` n `25`; metal avg `0.7957` n `20`; unknown avg `2.0464` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
