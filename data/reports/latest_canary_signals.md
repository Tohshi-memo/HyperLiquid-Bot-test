# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T16:22:30.708381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0109` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.9828` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.8219` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.2059` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0117` n `13`; crypto_alt avg `-0.6605` n `239`; crypto_major avg `-0.5644` n `8`; equity avg `-0.1822` n `162`; fx avg `-0.0072` n `6`; index avg `-0.0234` n `27`; metal avg `-0.0439` n `20`; unknown avg `-0.1041` n `1260`
- 1h: commodity avg `-0.0079` n `13`; crypto_alt avg `-0.9494` n `239`; crypto_major avg `-0.829` n `8`; equity avg `-0.3453` n `162`; fx avg `0.0034` n `6`; index avg `-0.0423` n `27`; metal avg `-0.1342` n `20`; unknown avg `159.4268` n `1254`
- 4h: commodity avg `-0.0541` n `13`; crypto_alt avg `-3.4384` n `239`; crypto_major avg `-3.065` n `8`; equity avg `-0.8591` n `162`; fx avg `-0.0023` n `6`; index avg `-0.0822` n `27`; metal avg `-0.2431` n `20`; unknown avg `-0.6321` n `1252`
- 24h: commodity avg `-0.1361` n `13`; crypto_alt avg `-6.2926` n `239`; crypto_major avg `-5.5455` n `8`; equity avg `-0.4831` n `162`; fx avg `-0.0845` n `6`; index avg `-0.008` n `27`; metal avg `-0.3588` n `20`; unknown avg `1.7143` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
