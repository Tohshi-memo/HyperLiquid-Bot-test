# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T02:52:13.041906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2717` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.0014` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0269` n `12`; crypto_alt avg `-0.0925` n `228`; crypto_major avg `-0.1781` n `8`; equity avg `-0.3389` n `66`; fx avg `-0.0009` n `5`; index avg `-0.1719` n `23`; metal avg `-0.1424` n `18`; unknown avg `0.0922` n `383`
- 1h: commodity avg `-0.0042` n `12`; crypto_alt avg `0.4278` n `228`; crypto_major avg `-0.0706` n `8`; equity avg `0.0947` n `66`; fx avg `0.0043` n `5`; index avg `-0.0271` n `23`; metal avg `-0.1719` n `18`; unknown avg `-0.4219` n `383`
- 4h: commodity avg `0.7998` n `12`; crypto_alt avg `-1.3011` n `228`; crypto_major avg `-1.4719` n `8`; equity avg `-0.6598` n `66`; fx avg `0.093` n `5`; index avg `-0.4705` n `23`; metal avg `-1.1286` n `18`; unknown avg `0.4763` n `383`
- 24h: commodity avg `2.6724` n `12`; crypto_alt avg `-10.884` n `228`; crypto_major avg `-3.4417` n `8`; equity avg `-3.0878` n `65`; fx avg `-0.0795` n `5`; index avg `-1.9175` n `23`; metal avg `-6.3163` n `18`; unknown avg `550.144` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
