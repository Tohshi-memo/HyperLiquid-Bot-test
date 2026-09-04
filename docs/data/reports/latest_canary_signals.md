# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T14:22:26.593150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.83` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.3234` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.9944` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8137` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1242` n `12`; crypto_alt avg `-0.2645` n `232`; crypto_major avg `-0.3208` n `8`; equity avg `-0.133` n `133`; fx avg `0.004` n `6`; index avg `-0.0182` n `26`; metal avg `0.0691` n `20`; unknown avg `0.9742` n `789`
- 1h: commodity avg `-0.0941` n `12`; crypto_alt avg `0.0252` n `232`; crypto_major avg `-0.3299` n `8`; equity avg `1.075` n `133`; fx avg `0.0249` n `6`; index avg `0.1411` n `26`; metal avg `0.1619` n `20`; unknown avg `-0.0306` n `785`
- 4h: commodity avg `-0.1102` n `12`; crypto_alt avg `-1.3951` n `232`; crypto_major avg `-1.9576` n `8`; equity avg `0.3658` n `133`; fx avg `-0.1172` n `6`; index avg `0.0368` n `26`; metal avg `-0.1439` n `20`; unknown avg `0.2713` n `737`
- 24h: commodity avg `-0.5487` n `12`; crypto_alt avg `0.2376` n `232`; crypto_major avg `0.1615` n `8`; equity avg `2.2355` n `133`; fx avg `-0.0748` n `6`; index avg `0.3259` n `26`; metal avg `-0.0027` n `20`; unknown avg `1.0797` n `698`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
