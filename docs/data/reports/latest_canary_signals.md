# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T05:37:19.653802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2102` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.1954` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1444` n `12`; crypto_alt avg `0.2566` n `228`; crypto_major avg `0.2075` n `8`; equity avg `0.3672` n `67`; fx avg `0.022` n `6`; index avg `0.1572` n `23`; metal avg `0.5402` n `18`; unknown avg `-0.1378` n `419`
- 1h: commodity avg `-0.255` n `12`; crypto_alt avg `-0.6371` n `228`; crypto_major avg `-0.2114` n `8`; equity avg `0.6205` n `67`; fx avg `0.0212` n `6`; index avg `0.2763` n `23`; metal avg `0.5113` n `18`; unknown avg `-0.6203` n `419`
- 4h: commodity avg `0.5115` n `12`; crypto_alt avg `-2.7071` n `228`; crypto_major avg `-1.6987` n `8`; equity avg `-1.0788` n `67`; fx avg `-0.0999` n `6`; index avg `-0.5033` n `23`; metal avg `-0.7877` n `18`; unknown avg `-1.043` n `419`
- 24h: commodity avg `0.1986` n `12`; crypto_alt avg `-4.9326` n `228`; crypto_major avg `-3.6982` n `8`; equity avg `-1.5268` n `67`; fx avg `-0.1099` n `6`; index avg `-1.1153` n `23`; metal avg `-2.3397` n `18`; unknown avg `-1.8908` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
