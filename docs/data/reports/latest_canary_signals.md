# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T06:56:32.251562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.68` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.4498` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.977` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5089` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2483` n `12`; crypto_alt avg `-0.3237` n `228`; crypto_major avg `-0.3063` n `8`; equity avg `-0.0282` n `69`; fx avg `0.0219` n `6`; index avg `-0.0267` n `23`; metal avg `0.0002` n `18`; unknown avg `1.0028` n `422`
- 1h: commodity avg `0.1639` n `12`; crypto_alt avg `-0.3044` n `228`; crypto_major avg `-0.4062` n `8`; equity avg `0.0756` n `69`; fx avg `0.0817` n `6`; index avg `-0.0265` n `23`; metal avg `0.234` n `18`; unknown avg `-0.235` n `412`
- 4h: commodity avg `-0.1897` n `12`; crypto_alt avg `-0.5877` n `228`; crypto_major avg `-1.1599` n `8`; equity avg `0.8171` n `69`; fx avg `0.1018` n `6`; index avg `0.349` n `23`; metal avg `1.2899` n `18`; unknown avg `-0.0986` n `412`
- 24h: commodity avg `-0.8797` n `12`; crypto_alt avg `-0.5734` n `228`; crypto_major avg `-1.8769` n `8`; equity avg `0.1582` n `69`; fx avg `0.1909` n `6`; index avg `-0.6481` n `23`; metal avg `1.2042` n `18`; unknown avg `2.8433` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
