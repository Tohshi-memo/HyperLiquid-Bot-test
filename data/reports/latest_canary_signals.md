# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T02:07:15.680948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8544` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3205` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1157` n `12`; crypto_alt avg `0.5479` n `228`; crypto_major avg `0.3687` n `8`; equity avg `-0.0616` n `66`; fx avg `0.015` n `5`; index avg `0.0033` n `23`; metal avg `-0.3839` n `18`; unknown avg `-0.2894` n `383`
- 1h: commodity avg `0.0897` n `12`; crypto_alt avg `0.2101` n `228`; crypto_major avg `-0.0446` n `8`; equity avg `0.2787` n `66`; fx avg `0.0364` n `5`; index avg `0.0387` n `23`; metal avg `0.4652` n `18`; unknown avg `-0.4605` n `383`
- 4h: commodity avg `1.0591` n `12`; crypto_alt avg `-1.8899` n `228`; crypto_major avg `-1.7953` n `8`; equity avg `-0.5078` n `66`; fx avg `0.1032` n `5`; index avg `-0.4748` n `23`; metal avg `-1.134` n `18`; unknown avg `0.2875` n `383`
- 24h: commodity avg `2.7992` n `12`; crypto_alt avg `-10.7781` n `228`; crypto_major avg `-3.0138` n `8`; equity avg `-3.2751` n `65`; fx avg `-0.0686` n `5`; index avg `-1.8875` n `23`; metal avg `-6.5089` n `18`; unknown avg `550.2134` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
