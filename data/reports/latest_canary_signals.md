# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T07:37:19.523839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0321` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.747` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.1017` n `228`; crypto_major avg `-0.26` n `8`; equity avg `-0.0888` n `69`; fx avg `-0.0164` n `6`; index avg `-0.0323` n `23`; metal avg `0.0319` n `18`; unknown avg `0.6484` n `422`
- 1h: commodity avg `0.1555` n `12`; crypto_alt avg `0.0254` n `228`; crypto_major avg `-0.3333` n `8`; equity avg `-0.0972` n `69`; fx avg `0.0347` n `6`; index avg `0.5456` n `23`; metal avg `0.0442` n `18`; unknown avg `0.846` n `422`
- 4h: commodity avg `0.5669` n `12`; crypto_alt avg `-2.0101` n `228`; crypto_major avg `-1.4652` n `8`; equity avg `-0.3669` n `69`; fx avg `-0.0697` n `6`; index avg `0.2818` n `23`; metal avg `-0.1285` n `18`; unknown avg `0.5071` n `412`
- 24h: commodity avg `1.2805` n `12`; crypto_alt avg `-0.0368` n `228`; crypto_major avg `-0.9166` n `8`; equity avg `-0.0946` n `69`; fx avg `-0.0351` n `6`; index avg `1.0498` n `23`; metal avg `0.1408` n `18`; unknown avg `2.2736` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2872`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2149`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
