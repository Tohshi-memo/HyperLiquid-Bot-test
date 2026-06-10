# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T19:22:39.019684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2918` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3155` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `-0.5696` n `228`; crypto_major avg `-0.4688` n `8`; equity avg `-0.6045` n `74`; fx avg `-0.0003` n `6`; index avg `-0.2142` n `23`; metal avg `-0.2868` n `18`; unknown avg `-0.1444` n `550`
- 1h: commodity avg `-0.0669` n `12`; crypto_alt avg `-0.4145` n `228`; crypto_major avg `-0.5419` n `8`; equity avg `-0.959` n `74`; fx avg `-0.014` n `6`; index avg `-0.4086` n `23`; metal avg `-0.6433` n `18`; unknown avg `0.3139` n `550`
- 4h: commodity avg `0.3212` n `12`; crypto_alt avg `-1.9092` n `228`; crypto_major avg `-1.9706` n `8`; equity avg `-1.2153` n `74`; fx avg `-0.0175` n `6`; index avg `-0.6551` n `23`; metal avg `-0.8357` n `18`; unknown avg `0.3271` n `548`
- 24h: commodity avg `1.2572` n `12`; crypto_alt avg `-1.6765` n `228`; crypto_major avg `-2.4788` n `8`; equity avg `-1.5354` n `74`; fx avg `-0.0505` n `6`; index avg `-0.8678` n `23`; metal avg `-2.0432` n `18`; unknown avg `-0.1616` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
