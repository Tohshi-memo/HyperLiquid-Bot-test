# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T22:52:26.297946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4044` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0015` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `-0.2413` n `228`; crypto_major avg `-0.1843` n `8`; equity avg `-0.0832` n `86`; fx avg `-0.0024` n `6`; index avg `0.0076` n `23`; metal avg `-0.0957` n `20`; unknown avg `-0.4456` n `764`
- 1h: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.0341` n `228`; crypto_major avg `-0.0535` n `8`; equity avg `0.1241` n `86`; fx avg `0.0095` n `6`; index avg `0.045` n `23`; metal avg `-0.0464` n `20`; unknown avg `-0.053` n `764`
- 4h: commodity avg `-0.0043` n `12`; crypto_alt avg `2.3353` n `228`; crypto_major avg `2.4001` n `8`; equity avg `2.9829` n `86`; fx avg `-0.0436` n `6`; index avg `0.7497` n `23`; metal avg `0.3986` n `20`; unknown avg `4.8436` n `764`
- 24h: commodity avg `-0.5148` n `12`; crypto_alt avg `-2.4463` n `228`; crypto_major avg `-2.0092` n `8`; equity avg `4.5662` n `86`; fx avg `0.0377` n `6`; index avg `0.6696` n `23`; metal avg `-1.5864` n `20`; unknown avg `-0.7737` n `724`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
