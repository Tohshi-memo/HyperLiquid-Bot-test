# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T05:52:26.424420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0999` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0056` n `13`; crypto_alt avg `0.0437` n `239`; crypto_major avg `0.0363` n `8`; equity avg `0.0815` n `168`; fx avg `0.0011` n `6`; index avg `-0.0047` n `27`; metal avg `0.0179` n `20`; unknown avg `1.3979` n `1263`
- 1h: commodity avg `0.0587` n `13`; crypto_alt avg `0.1793` n `239`; crypto_major avg `0.3816` n `8`; equity avg `0.8765` n `168`; fx avg `0.0193` n `6`; index avg `0.0359` n `27`; metal avg `0.2129` n `20`; unknown avg `5.5123` n `1253`
- 4h: commodity avg `0.181` n `13`; crypto_alt avg `1.4688` n `239`; crypto_major avg `2.2809` n `8`; equity avg `2.9197` n `168`; fx avg `-0.0027` n `6`; index avg `0.2235` n `27`; metal avg `0.8196` n `20`; unknown avg `68.3059` n `1249`
- 24h: commodity avg `0.3111` n `13`; crypto_alt avg `1.8551` n `239`; crypto_major avg `2.2827` n `8`; equity avg `3.6086` n `168`; fx avg `0.0255` n `6`; index avg `0.2911` n `27`; metal avg `0.9697` n `20`; unknown avg `211.3191` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
