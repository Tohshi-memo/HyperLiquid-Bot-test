# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T19:16:16.318002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7413` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4779` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0028` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0442` n `12`; crypto_alt avg `-0.3284` n `228`; crypto_major avg `-0.3473` n `8`; equity avg `-0.0433` n `86`; fx avg `-0.0056` n `6`; index avg `-0.014` n `23`; metal avg `-0.0233` n `20`; unknown avg `-0.1923` n `764`
- 1h: commodity avg `-0.0738` n `12`; crypto_alt avg `-0.5752` n `228`; crypto_major avg `-0.6886` n `8`; equity avg `-0.8208` n `86`; fx avg `0.0112` n `6`; index avg `-0.1068` n `23`; metal avg `-0.0918` n `20`; unknown avg `-0.3026` n `764`
- 4h: commodity avg `0.0062` n `12`; crypto_alt avg `-3.0408` n `228`; crypto_major avg `-2.7351` n `8`; equity avg `-1.8824` n `86`; fx avg `0.0155` n `6`; index avg `-0.2572` n `23`; metal avg `-0.7323` n `20`; unknown avg `-0.7927` n `764`
- 24h: commodity avg `-0.5519` n `12`; crypto_alt avg `-4.2438` n `228`; crypto_major avg `-3.9244` n `8`; equity avg `1.613` n `86`; fx avg `0.0673` n `6`; index avg `-0.0566` n `23`; metal avg `-2.0607` n `20`; unknown avg `-0.2778` n `724`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
