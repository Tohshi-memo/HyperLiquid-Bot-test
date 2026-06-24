# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T17:07:33.065678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.4982` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.3276` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.2792` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6113` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0362` n `12`; crypto_alt avg `-0.0303` n `228`; crypto_major avg `-0.1603` n `8`; equity avg `-0.3929` n `86`; fx avg `0.0044` n `6`; index avg `-0.0565` n `23`; metal avg `-0.0714` n `20`; unknown avg `0.0208` n `764`
- 1h: commodity avg `0.0677` n `12`; crypto_alt avg `-1.7683` n `228`; crypto_major avg `-1.0318` n `8`; equity avg `-0.7262` n `86`; fx avg `0.0244` n `6`; index avg `-0.1033` n `23`; metal avg `-0.0592` n `20`; unknown avg `-0.1699` n `764`
- 4h: commodity avg `0.107` n `12`; crypto_alt avg `-3.6507` n `228`; crypto_major avg `-3.3912` n `8`; equity avg `-1.7799` n `86`; fx avg `0.0292` n `6`; index avg `-0.112` n `23`; metal avg `-0.0636` n `20`; unknown avg `0.4775` n `764`
- 24h: commodity avg `-0.4153` n `12`; crypto_alt avg `-3.8996` n `228`; crypto_major avg `-3.5823` n `8`; equity avg `1.8093` n `86`; fx avg `0.0626` n `6`; index avg `-0.0016` n `23`; metal avg `-1.7065` n `20`; unknown avg `0.0315` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
