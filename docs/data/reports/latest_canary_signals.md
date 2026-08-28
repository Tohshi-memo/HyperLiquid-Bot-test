# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T19:07:23.046183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5882` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3305` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7392` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `0.4521` n `231`; crypto_major avg `0.4864` n `8`; equity avg `0.1211` n `127`; fx avg `-0.0017` n `6`; index avg `0.0171` n `26`; metal avg `0.0247` n `20`; unknown avg `1.5888` n `793`
- 1h: commodity avg `0.0535` n `12`; crypto_alt avg `-0.3587` n `231`; crypto_major avg `-0.4917` n `8`; equity avg `-0.2136` n `127`; fx avg `0.0002` n `6`; index avg `-0.0309` n `26`; metal avg `-0.0445` n `20`; unknown avg `1.3549` n `793`
- 4h: commodity avg `-0.014` n `12`; crypto_alt avg `-2.5043` n `231`; crypto_major avg `-2.6022` n `8`; equity avg `-1.4336` n `127`; fx avg `-0.0318` n `6`; index avg `-0.2717` n `26`; metal avg `-0.863` n `20`; unknown avg `1.7987` n `793`
- 24h: commodity avg `-0.2222` n `12`; crypto_alt avg `-3.7361` n `231`; crypto_major avg `-4.1196` n `8`; equity avg `-2.2671` n `127`; fx avg `-0.1136` n `6`; index avg `-0.1344` n `26`; metal avg `-0.4153` n `20`; unknown avg `-0.5694` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
