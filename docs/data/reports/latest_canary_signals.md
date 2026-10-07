# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T11:37:34.347423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1606` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0116` n `13`; crypto_alt avg `-0.1775` n `235`; crypto_major avg `-0.1303` n `8`; equity avg `-0.0178` n `150`; fx avg `-0.0086` n `6`; index avg `-0.0164` n `26`; metal avg `0.0164` n `20`; unknown avg `2.2187` n `1076`
- 1h: commodity avg `0.1742` n `13`; crypto_alt avg `-0.4374` n `235`; crypto_major avg `-0.1766` n `8`; equity avg `-0.3227` n `150`; fx avg `-0.0218` n `6`; index avg `-0.0695` n `26`; metal avg `0.0093` n `20`; unknown avg `1.0224` n `1074`
- 4h: commodity avg `0.2649` n `13`; crypto_alt avg `-1.8414` n `235`; crypto_major avg `-1.3223` n `8`; equity avg `-0.9256` n `150`; fx avg `-0.049` n `6`; index avg `-0.1617` n `26`; metal avg `-0.2122` n `20`; unknown avg `2.1515` n `1058`
- 24h: commodity avg `1.3994` n `13`; crypto_alt avg `-5.4018` n `235`; crypto_major avg `-3.6544` n `8`; equity avg `-1.6047` n `150`; fx avg `-0.1556` n `6`; index avg `-0.3613` n `26`; metal avg `-0.5304` n `20`; unknown avg `815.5781` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
