# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T01:07:15.159251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6289` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2132` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2151` n `12`; crypto_alt avg `0.3105` n `228`; crypto_major avg `0.1755` n `8`; equity avg `0.2808` n `66`; fx avg `0.0205` n `5`; index avg `0.0875` n `23`; metal avg `-0.206` n `18`; unknown avg `0.5465` n `383`
- 1h: commodity avg `0.4924` n `12`; crypto_alt avg `0.5323` n `228`; crypto_major avg `0.0395` n `8`; equity avg `0.1302` n `66`; fx avg `0.0248` n `5`; index avg `0.1685` n `23`; metal avg `-1.3711` n `18`; unknown avg `0.519` n `383`
- 4h: commodity avg `0.9916` n `12`; crypto_alt avg `-1.9791` n `228`; crypto_major avg `-1.6373` n `8`; equity avg `-0.5898` n `66`; fx avg `0.0755` n `5`; index avg `-0.4241` n `23`; metal avg `-1.0499` n `18`; unknown avg `1.6777` n `383`
- 24h: commodity avg `2.7038` n `12`; crypto_alt avg `-10.9528` n `228`; crypto_major avg `-2.9426` n `8`; equity avg `-3.5741` n `65`; fx avg `-0.1051` n `5`; index avg `-1.9255` n `23`; metal avg `-6.9353` n `18`; unknown avg `550.8289` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
