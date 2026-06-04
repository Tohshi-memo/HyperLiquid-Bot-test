# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T03:22:25.534677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.5594` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.0229` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `0.2411` n `228`; crypto_major avg `0.0353` n `8`; equity avg `0.0065` n `73`; fx avg `0.0062` n `6`; index avg `0.0238` n `23`; metal avg `-0.1442` n `18`; unknown avg `0.5114` n `420`
- 1h: commodity avg `-0.0342` n `12`; crypto_alt avg `2.2548` n `228`; crypto_major avg `1.7442` n `8`; equity avg `0.6536` n `73`; fx avg `0.0097` n `6`; index avg `0.1806` n `23`; metal avg `0.1848` n `18`; unknown avg `0.9169` n `420`
- 4h: commodity avg `-0.4489` n `12`; crypto_alt avg `-2.3972` n `228`; crypto_major avg `-0.9192` n `8`; equity avg `0.4713` n `73`; fx avg `-0.024` n `6`; index avg `0.1037` n `23`; metal avg `0.3636` n `18`; unknown avg `-0.5692` n `419`
- 24h: commodity avg `-0.0397` n `12`; crypto_alt avg `-1.2428` n `228`; crypto_major avg `-1.7051` n `8`; equity avg `-3.3883` n `73`; fx avg `-0.0057` n `6`; index avg `-1.1421` n `23`; metal avg `-1.7167` n `18`; unknown avg `0.5798` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
