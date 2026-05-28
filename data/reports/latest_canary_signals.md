# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T04:36:00.984865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3575` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.0583` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `0.6332` n `228`; crypto_major avg `0.4722` n `8`; equity avg `0.2918` n `67`; fx avg `-0.0031` n `6`; index avg `0.0385` n `23`; metal avg `-0.1491` n `18`; unknown avg `-0.1759` n `419`
- 1h: commodity avg `0.1049` n `12`; crypto_alt avg `-0.8666` n `228`; crypto_major avg `-0.4228` n `8`; equity avg `-0.3724` n `67`; fx avg `-0.0673` n `6`; index avg `-0.2397` n `23`; metal avg `-0.3047` n `18`; unknown avg `-0.7352` n `419`
- 4h: commodity avg `0.615` n `12`; crypto_alt avg `-2.648` n `228`; crypto_major avg `-1.7425` n `8`; equity avg `-1.5784` n `67`; fx avg `-0.1225` n `6`; index avg `-0.6842` n `23`; metal avg `-1.9524` n `18`; unknown avg `-0.2355` n `419`
- 24h: commodity avg `0.3736` n `12`; crypto_alt avg `-3.5145` n `228`; crypto_major avg `-2.6992` n `8`; equity avg `-2.0362` n `67`; fx avg `-0.1219` n `6`; index avg `-1.3736` n `23`; metal avg `-2.9894` n `18`; unknown avg `-1.2785` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
