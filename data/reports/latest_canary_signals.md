# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T02:22:29.735559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5011` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.1587` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0561` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0214` n `13`; crypto_alt avg `-1.6194` n `236`; crypto_major avg `-1.1232` n `8`; equity avg `-0.0467` n `151`; fx avg `-0.0139` n `6`; index avg `0.0107` n `26`; metal avg `0.0334` n `20`; unknown avg `9.0039` n `1136`
- 1h: commodity avg `-0.0203` n `13`; crypto_alt avg `-1.7075` n `236`; crypto_major avg `-1.1541` n `8`; equity avg `-0.0164` n `151`; fx avg `0.0055` n `6`; index avg `0.0046` n `26`; metal avg `-0.0808` n `20`; unknown avg `8.8703` n `1134`
- 4h: commodity avg `-0.3151` n `13`; crypto_alt avg `-2.3638` n `236`; crypto_major avg `-1.3344` n `8`; equity avg `-0.7273` n `151`; fx avg `0.2366` n `6`; index avg `-0.2783` n `26`; metal avg `0.1667` n `20`; unknown avg `8.2712` n `1128`
- 24h: commodity avg `-0.4679` n `13`; crypto_alt avg `-4.9117` n `236`; crypto_major avg `-3.6763` n `8`; equity avg `-5.9431` n `151`; fx avg `0.076` n `6`; index avg `-0.9828` n `26`; metal avg `-0.672` n `20`; unknown avg `1395.9753` n `890`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1271`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1156`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1017`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0816`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0735`, n `666`, weak_sample_signal
