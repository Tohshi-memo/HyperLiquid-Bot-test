# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T14:52:29.339619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2742` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2918` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.0128` n `228`; crypto_major avg `-0.1249` n `8`; equity avg `0.1044` n `69`; fx avg `-0.0048` n `6`; index avg `-0.0041` n `23`; metal avg `-0.0605` n `18`; unknown avg `-0.2026` n `422`
- 1h: commodity avg `0.3624` n `12`; crypto_alt avg `-0.1132` n `228`; crypto_major avg `-0.4309` n `8`; equity avg `0.1157` n `69`; fx avg `0.0203` n `6`; index avg `-0.1536` n `23`; metal avg `0.073` n `18`; unknown avg `-0.349` n `422`
- 4h: commodity avg `0.5367` n `12`; crypto_alt avg `-1.0686` n `228`; crypto_major avg `-1.7375` n `8`; equity avg `-0.5671` n `69`; fx avg `-0.0781` n `6`; index avg `-0.4457` n `23`; metal avg `-1.0134` n `18`; unknown avg `1.5268` n `416`
- 24h: commodity avg `1.4644` n `12`; crypto_alt avg `-0.4315` n `228`; crypto_major avg `-1.8164` n `8`; equity avg `-0.6561` n `69`; fx avg `-0.0701` n `6`; index avg `0.1248` n `23`; metal avg `-0.6929` n `18`; unknown avg `3.3811` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2827`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
