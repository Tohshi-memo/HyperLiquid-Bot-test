# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T17:37:36.721590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4977` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0071` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0537` n `12`; crypto_alt avg `-0.0825` n `228`; crypto_major avg `-0.253` n `8`; equity avg `-0.0504` n `86`; fx avg `-0.0093` n `6`; index avg `0.0036` n `23`; metal avg `-0.0557` n `20`; unknown avg `0.2225` n `765`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `-0.1309` n `228`; crypto_major avg `-0.3722` n `8`; equity avg `-0.0039` n `86`; fx avg `0.0043` n `6`; index avg `-0.003` n `23`; metal avg `-0.0894` n `20`; unknown avg `0.3716` n `765`
- 4h: commodity avg `-0.0711` n `12`; crypto_alt avg `2.5259` n `228`; crypto_major avg `2.4266` n `8`; equity avg `1.6295` n `86`; fx avg `-0.0626` n `6`; index avg `0.2595` n `23`; metal avg `0.4195` n `20`; unknown avg `0.611` n `765`
- 24h: commodity avg `-0.373` n `12`; crypto_alt avg `2.0713` n `228`; crypto_major avg `1.7342` n `8`; equity avg `-0.297` n `86`; fx avg `-0.0678` n `6`; index avg `-0.1921` n `23`; metal avg `0.5246` n `20`; unknown avg `0.2692` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
