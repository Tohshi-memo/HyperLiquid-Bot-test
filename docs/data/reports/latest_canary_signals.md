# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T20:07:29.750163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.129` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3896` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1835` n `12`; crypto_alt avg `-0.3294` n `228`; crypto_major avg `-0.2144` n `8`; equity avg `-0.6007` n `74`; fx avg `-0.0128` n `6`; index avg `-0.1503` n `23`; metal avg `-0.2672` n `18`; unknown avg `-0.0465` n `550`
- 1h: commodity avg `0.1511` n `12`; crypto_alt avg `-1.0345` n `228`; crypto_major avg `-0.5418` n `8`; equity avg `-0.9841` n `74`; fx avg `-0.0171` n `6`; index avg `-0.4327` n `23`; metal avg `-0.6923` n `18`; unknown avg `-0.297` n `550`
- 4h: commodity avg `-0.2776` n `12`; crypto_alt avg `-2.5651` n `228`; crypto_major avg `-2.4066` n `8`; equity avg `-1.8859` n `74`; fx avg `-0.0139` n `6`; index avg `-1.017` n `23`; metal avg `-1.3804` n `18`; unknown avg `4.7069` n `548`
- 24h: commodity avg `1.2797` n `12`; crypto_alt avg `-2.4375` n `228`; crypto_major avg `-2.6833` n `8`; equity avg `-2.4097` n `74`; fx avg `-0.0184` n `6`; index avg `-1.522` n `23`; metal avg `-2.505` n `18`; unknown avg `-0.56` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
