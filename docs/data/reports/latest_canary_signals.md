# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T00:52:16.247638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5374` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2813` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1584` n `12`; crypto_alt avg `-0.0204` n `228`; crypto_major avg `-0.1196` n `8`; equity avg `-0.0603` n `66`; fx avg `0.0099` n `5`; index avg `0.0293` n `23`; metal avg `-0.1146` n `18`; unknown avg `0.4704` n `383`
- 1h: commodity avg `0.4413` n `12`; crypto_alt avg `0.2344` n `228`; crypto_major avg `0.0022` n `8`; equity avg `-0.9792` n `66`; fx avg `0.0167` n `5`; index avg `-0.3091` n `23`; metal avg `-1.4169` n `18`; unknown avg `0.0278` n `383`
- 4h: commodity avg `0.7217` n `12`; crypto_alt avg `-2.3287` n `228`; crypto_major avg `-1.8157` n `8`; equity avg `-0.924` n `66`; fx avg `0.0306` n `5`; index avg `-0.5344` n `23`; metal avg `-0.8692` n `18`; unknown avg `2.4405` n `383`
- 24h: commodity avg `2.4793` n `12`; crypto_alt avg `-11.2179` n `228`; crypto_major avg `-3.1098` n `8`; equity avg `-3.8095` n `65`; fx avg `-0.1257` n `5`; index avg `-2.0096` n `23`; metal avg `-6.7468` n `18`; unknown avg `550.4346` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
