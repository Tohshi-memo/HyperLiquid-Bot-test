# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T18:52:29.444384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2669` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.9645` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.4583` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6793` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.255` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.0707` n `231`; crypto_major avg `-0.2215` n `8`; equity avg `-0.1963` n `127`; fx avg `-0.0047` n `6`; index avg `-0.03` n `26`; metal avg `-0.0134` n `20`; unknown avg `-0.1106` n `793`
- 1h: commodity avg `-0.0758` n `12`; crypto_alt avg `-1.1505` n `231`; crypto_major avg `-1.3135` n `8`; equity avg `-0.3877` n `127`; fx avg `-0.001` n `6`; index avg `-0.0585` n `26`; metal avg `-0.1798` n `20`; unknown avg `-0.4597` n `793`
- 4h: commodity avg `0.0213` n `12`; crypto_alt avg `-3.0422` n `231`; crypto_major avg `-3.2456` n `8`; equity avg `-1.5663` n `127`; fx avg `-0.0184` n `6`; index avg `-0.2811` n `26`; metal avg `-0.7873` n `20`; unknown avg `0.3061` n `793`
- 24h: commodity avg `-0.2394` n `12`; crypto_alt avg `-3.9406` n `231`; crypto_major avg `-4.0826` n `8`; equity avg `-2.2954` n `127`; fx avg `-0.1102` n `6`; index avg `-0.1227` n `26`; metal avg `-0.3855` n `20`; unknown avg `-0.6445` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
