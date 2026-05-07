# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T16:22:19.186476+00:00`
- Correlation status: `ready`
- Asset price records: `565`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2498` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.4289` n `12`; crypto_alt avg `0.3804` n `228`; crypto_major avg `0.1856` n `8`; equity avg `-0.3011` n `65`; fx avg `0.0023` n `5`; index avg `-0.1514` n `23`; metal avg `-0.1492` n `18`; unknown avg `0.0205` n `365`
- 1h: commodity avg `1.1393` n `12`; crypto_alt avg `0.3401` n `228`; crypto_major avg `-0.038` n `8`; equity avg `-1.0939` n `65`; fx avg `0.046` n `5`; index avg `-0.583` n `23`; metal avg `-1.0823` n `18`; unknown avg `-0.2837` n `365`
- 4h: commodity avg `1.7044` n `12`; crypto_alt avg `-1.2081` n `228`; crypto_major avg `-1.5454` n `8`; equity avg `-1.6986` n `65`; fx avg `0.0647` n `5`; index avg `-0.8404` n `23`; metal avg `-1.2428` n `18`; unknown avg `-0.7815` n `365`
- 24h: commodity avg `0.467` n `12`; crypto_alt avg `0.1534` n `228`; crypto_major avg `-2.0379` n `8`; equity avg `-0.6065` n `65`; fx avg `0.1474` n `5`; index avg `-0.2646` n `23`; metal avg `0.6352` n `18`; unknown avg `-0.7045` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1304`, n `561`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `561`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `561`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `561`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0958`, n `557`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0906`, n `557`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `557`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.083`, n `557`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `561`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.076`, n `557`, weak_sample_signal
