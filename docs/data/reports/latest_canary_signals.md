# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T19:37:29.674993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0246` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2662` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0263` n `12`; crypto_alt avg `0.14` n `228`; crypto_major avg `0.4392` n `8`; equity avg `0.4734` n `74`; fx avg `-0.0054` n `6`; index avg `0.0349` n `23`; metal avg `-0.1302` n `18`; unknown avg `0.089` n `550`
- 1h: commodity avg `0.0698` n `12`; crypto_alt avg `-0.1079` n `228`; crypto_major avg `0.1329` n `8`; equity avg `-0.2471` n `74`; fx avg `-0.0131` n `6`; index avg `-0.2077` n `23`; metal avg `-0.6772` n `18`; unknown avg `0.0377` n `550`
- 4h: commodity avg `0.2306` n `12`; crypto_alt avg `-1.8697` n `228`; crypto_major avg `-1.794` n `8`; equity avg `-0.7064` n `74`; fx avg `-0.0194` n `6`; index avg `-0.5278` n `23`; metal avg `-0.9852` n `18`; unknown avg `0.4821` n `548`
- 24h: commodity avg `1.1928` n `12`; crypto_alt avg `-1.6881` n `228`; crypto_major avg `-2.2088` n `8`; equity avg `-1.15` n `74`; fx avg `-0.0483` n `6`; index avg `-0.8545` n `23`; metal avg `-2.1654` n `18`; unknown avg `-0.0213` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
