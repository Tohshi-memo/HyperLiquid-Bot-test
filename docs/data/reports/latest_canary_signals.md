# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T03:22:14.190298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1734` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2361` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.046` n `12`; crypto_alt avg `-0.3147` n `228`; crypto_major avg `-0.4303` n `8`; equity avg `-0.16` n `66`; fx avg `-0.0001` n `5`; index avg `0.0069` n `23`; metal avg `-0.0203` n `18`; unknown avg `-0.1178` n `383`
- 1h: commodity avg `-0.0547` n `12`; crypto_alt avg `0.0078` n `228`; crypto_major avg `-0.3815` n `8`; equity avg `-0.2529` n `66`; fx avg `-0.0218` n `5`; index avg `-0.054` n `23`; metal avg `-0.1424` n `18`; unknown avg `-0.4182` n `383`
- 4h: commodity avg `0.6789` n `12`; crypto_alt avg `-0.98` n `228`; crypto_major avg `-1.4945` n `8`; equity avg `-0.3449` n `66`; fx avg `0.0977` n `5`; index avg `-0.2584` n `23`; metal avg `-1.0755` n `18`; unknown avg `-0.2451` n `383`
- 24h: commodity avg `2.6328` n `12`; crypto_alt avg `-10.8289` n `228`; crypto_major avg `-3.5671` n `8`; equity avg `-3.1598` n `65`; fx avg `-0.0762` n `5`; index avg `-1.8171` n `23`; metal avg `-6.4109` n `18`; unknown avg `550.0586` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
