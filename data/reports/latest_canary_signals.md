# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T06:57:42.829612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7213` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7203` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.1521` n `230`; crypto_major avg `-0.3095` n `8`; equity avg `-0.0252` n `121`; fx avg `-0.0806` n `6`; index avg `-0.0019` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.0164` n `794`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `0.448` n `230`; crypto_major avg `0.0831` n `8`; equity avg `-0.0265` n `121`; fx avg `-0.0282` n `6`; index avg `-0.0204` n `25`; metal avg `-0.0132` n `20`; unknown avg `0.1782` n `778`
- 4h: commodity avg `-0.0284` n `12`; crypto_alt avg `-1.666` n `230`; crypto_major avg `-1.7517` n `8`; equity avg `-0.2567` n `121`; fx avg `-0.0559` n `6`; index avg `-0.0314` n `25`; metal avg `-0.0304` n `20`; unknown avg `0.1523` n `778`
- 24h: commodity avg `-0.0185` n `12`; crypto_alt avg `-4.4298` n `230`; crypto_major avg `-2.6493` n `8`; equity avg `-0.196` n `121`; fx avg `0.0358` n `6`; index avg `-0.0295` n `25`; metal avg `0.0647` n `20`; unknown avg `3.2677` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
