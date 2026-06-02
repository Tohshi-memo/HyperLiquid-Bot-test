# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T22:07:25.575716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.49` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.2478` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8518` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6161` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1715` n `12`; crypto_alt avg `-0.3539` n `228`; crypto_major avg `-0.2107` n `8`; equity avg `0.1735` n `69`; fx avg `-0.0029` n `6`; index avg `-0.0355` n `23`; metal avg `0.0054` n `18`; unknown avg `-0.4481` n `422`
- 1h: commodity avg `0.1581` n `12`; crypto_alt avg `-0.4462` n `228`; crypto_major avg `-0.4491` n `8`; equity avg `0.1306` n `69`; fx avg `-0.0088` n `6`; index avg `-0.0043` n `23`; metal avg `0.0074` n `18`; unknown avg `-0.2161` n `422`
- 4h: commodity avg `0.1489` n `12`; crypto_alt avg `-1.3251` n `228`; crypto_major avg `-1.5495` n `8`; equity avg `0.6983` n `69`; fx avg `-0.0165` n `6`; index avg `0.3023` n `23`; metal avg `0.0666` n `18`; unknown avg `-0.3836` n `422`
- 24h: commodity avg `0.0012` n `12`; crypto_alt avg `-3.1406` n `228`; crypto_major avg `-4.5163` n `8`; equity avg `1.4233` n `69`; fx avg `0.0742` n `6`; index avg `0.8035` n `23`; metal avg `0.4981` n `18`; unknown avg `-0.1859` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
