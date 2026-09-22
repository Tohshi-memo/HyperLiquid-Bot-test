# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T02:22:30.604484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5047` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2982` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0454` n `12`; crypto_alt avg `-0.1852` n `234`; crypto_major avg `-0.1899` n `8`; equity avg `0.0015` n `140`; fx avg `0.0022` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0077` n `20`; unknown avg `-0.0519` n `944`
- 1h: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0258` n `234`; crypto_major avg `0.0129` n `8`; equity avg `0.0418` n `140`; fx avg `-0.0218` n `6`; index avg `0.0014` n `26`; metal avg `-0.026` n `20`; unknown avg `-0.1479` n `942`
- 4h: commodity avg `0.1731` n `12`; crypto_alt avg `0.1299` n `234`; crypto_major avg `-1.2736` n `8`; equity avg `0.2311` n `140`; fx avg `-0.1589` n `6`; index avg `0.0246` n `26`; metal avg `-0.042` n `20`; unknown avg `0.9527` n `936`
- 24h: commodity avg `-0.2145` n `12`; crypto_alt avg `3.9857` n `234`; crypto_major avg `4.2283` n `8`; equity avg `2.4128` n `140`; fx avg `-0.2392` n `6`; index avg `0.5062` n `26`; metal avg `-0.0117` n `20`; unknown avg `11.8341` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
