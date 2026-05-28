# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T05:22:17.652712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6065` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2905` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `-0.7419` n `228`; crypto_major avg `-0.4205` n `8`; equity avg `0.307` n `67`; fx avg `0.0031` n `6`; index avg `0.0982` n `23`; metal avg `0.005` n `18`; unknown avg `-0.2415` n `419`
- 1h: commodity avg `-0.1175` n `12`; crypto_alt avg `-0.2651` n `228`; crypto_major avg `0.0521` n `8`; equity avg `0.5449` n `67`; fx avg `-0.004` n `6`; index avg `0.1574` n `23`; metal avg `-0.1776` n `18`; unknown avg `-0.6866` n `419`
- 4h: commodity avg `0.6522` n `12`; crypto_alt avg `-3.0921` n `228`; crypto_major avg `-1.9543` n `8`; equity avg `-1.5337` n `67`; fx avg `-0.104` n `6`; index avg `-0.6638` n `23`; metal avg `-1.4281` n `18`; unknown avg `-1.0768` n `419`
- 24h: commodity avg `0.2328` n `12`; crypto_alt avg `-5.0741` n `228`; crypto_major avg `-3.7079` n `8`; equity avg `-1.8261` n `67`; fx avg `-0.1332` n `6`; index avg `-1.2537` n `23`; metal avg `-3.1005` n `18`; unknown avg `-1.9108` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1722`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
