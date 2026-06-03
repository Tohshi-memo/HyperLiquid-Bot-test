# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T01:07:23.408971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.45` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2857` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1577` n `12`; crypto_alt avg `-0.0214` n `228`; crypto_major avg `-0.1276` n `8`; equity avg `-0.2023` n `69`; fx avg `0.0066` n `6`; index avg `0.15` n `23`; metal avg `-0.5315` n `18`; unknown avg `-0.2378` n `422`
- 1h: commodity avg `0.1595` n `12`; crypto_alt avg `0.9026` n `228`; crypto_major avg `0.3981` n `8`; equity avg `-0.0192` n `69`; fx avg `0.0424` n `6`; index avg `0.2912` n `23`; metal avg `-0.2704` n `18`; unknown avg `-0.2323` n `422`
- 4h: commodity avg `0.5187` n `12`; crypto_alt avg `-0.9431` n `228`; crypto_major avg `-0.9005` n `8`; equity avg `-0.3165` n `69`; fx avg `0.0204` n `6`; index avg `0.3852` n `23`; metal avg `-0.4629` n `18`; unknown avg `-0.5581` n `422`
- 24h: commodity avg `0.7133` n `12`; crypto_alt avg `-3.8824` n `228`; crypto_major avg `-5.448` n `8`; equity avg `1.7287` n `69`; fx avg `0.1059` n `6`; index avg `1.5647` n `23`; metal avg `-0.1836` n `18`; unknown avg `-0.4826` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
