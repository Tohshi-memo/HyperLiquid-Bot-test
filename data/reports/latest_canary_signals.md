# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T18:22:29.158628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1281` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9735` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6232` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.026` n `12`; crypto_alt avg `0.9868` n `228`; crypto_major avg `0.9266` n `8`; equity avg `0.4356` n `86`; fx avg `-0.0028` n `6`; index avg `0.0558` n `23`; metal avg `0.1192` n `20`; unknown avg `1.2156` n `764`
- 1h: commodity avg `0.0189` n `12`; crypto_alt avg `1.589` n `228`; crypto_major avg `1.1289` n `8`; equity avg `0.3915` n `86`; fx avg `-0.0076` n `6`; index avg `0.017` n `23`; metal avg `-0.2889` n `20`; unknown avg `3.3667` n `764`
- 4h: commodity avg `0.0811` n `12`; crypto_alt avg `-2.3621` n `228`; crypto_major avg `-2.047` n `8`; equity avg `-0.4238` n `86`; fx avg `0.028` n `6`; index avg `-0.0735` n `23`; metal avg `-0.7484` n `20`; unknown avg `-0.2717` n `764`
- 24h: commodity avg `-0.4178` n `12`; crypto_alt avg `-3.6809` n `228`; crypto_major avg `-3.4695` n `8`; equity avg `2.0318` n `86`; fx avg `0.0662` n `6`; index avg `0.0266` n `23`; metal avg `-2.0299` n `20`; unknown avg `0.0133` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
