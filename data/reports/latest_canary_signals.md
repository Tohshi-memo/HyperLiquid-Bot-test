# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T14:08:55.092187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.0073` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.0163` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0473` n `12`; crypto_alt avg `-0.0317` n `228`; crypto_major avg `-0.1195` n `8`; equity avg `0.0057` n `69`; fx avg `0.0115` n `6`; index avg `-0.0546` n `23`; metal avg `-0.0128` n `18`; unknown avg `-0.1381` n `422`
- 1h: commodity avg `1.1144` n `12`; crypto_alt avg `-0.2232` n `228`; crypto_major avg `-0.8929` n `8`; equity avg `-0.2919` n `69`; fx avg `-0.0581` n `6`; index avg `-0.1388` n `23`; metal avg `-0.9139` n `18`; unknown avg `-0.2125` n `422`
- 4h: commodity avg `0.1051` n `12`; crypto_alt avg `-0.7679` n `228`; crypto_major avg `-1.2649` n `8`; equity avg `-0.5639` n `69`; fx avg `-0.0895` n `6`; index avg `-0.2486` n `23`; metal avg `-0.9842` n `18`; unknown avg `2.3286` n `416`
- 24h: commodity avg `1.1843` n `12`; crypto_alt avg `-1.0975` n `228`; crypto_major avg `-1.9608` n `8`; equity avg `-0.8364` n `69`; fx avg `-0.0825` n `6`; index avg `0.2363` n `23`; metal avg `-0.7812` n `18`; unknown avg `4.263` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2826`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
