# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T17:52:26.569915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.77` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.3081` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.3016` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.9691` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `-0.3132` n `228`; crypto_major avg `-0.1081` n `8`; equity avg `0.038` n `69`; fx avg `-0.0067` n `6`; index avg `-0.0145` n `23`; metal avg `-0.0293` n `18`; unknown avg `0.504` n `422`
- 1h: commodity avg `0.1771` n `12`; crypto_alt avg `0.2897` n `228`; crypto_major avg `0.1463` n `8`; equity avg `-0.2595` n `69`; fx avg `-0.0236` n `6`; index avg `-0.1137` n `23`; metal avg `-0.2606` n `18`; unknown avg `0.4127` n `422`
- 4h: commodity avg `0.4959` n `12`; crypto_alt avg `-1.8229` n `228`; crypto_major avg `-1.8122` n `8`; equity avg `0.4894` n `69`; fx avg `-0.0085` n `6`; index avg `0.1569` n `23`; metal avg `-0.4567` n `18`; unknown avg `-0.397` n `422`
- 24h: commodity avg `0.4089` n `12`; crypto_alt avg `-2.8876` n `228`; crypto_major avg `-3.4643` n `8`; equity avg `-0.2097` n `69`; fx avg `0.07` n `6`; index avg `0.0275` n `23`; metal avg `0.0137` n `18`; unknown avg `-0.5019` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
