# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T18:07:36.661182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1258` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1079` n `12`; crypto_alt avg `-0.3509` n `231`; crypto_major avg `-0.3471` n `8`; equity avg `-0.0541` n `127`; fx avg `-0.0029` n `6`; index avg `-0.0105` n `26`; metal avg `-0.111` n `20`; unknown avg `-0.1827` n `793`
- 1h: commodity avg `-0.0984` n `12`; crypto_alt avg `-0.2133` n `231`; crypto_major avg `-0.358` n `8`; equity avg `0.1926` n `127`; fx avg `-0.0099` n `6`; index avg `0.0438` n `26`; metal avg `-0.0965` n `20`; unknown avg `-0.2843` n `793`
- 4h: commodity avg `0.0657` n `12`; crypto_alt avg `-1.0747` n `231`; crypto_major avg `-1.2354` n `8`; equity avg `-0.7651` n `127`; fx avg `0.0089` n `6`; index avg `-0.1096` n `26`; metal avg `-0.5244` n `20`; unknown avg `0.0922` n `793`
- 24h: commodity avg `-0.4348` n `12`; crypto_alt avg `-3.6802` n `231`; crypto_major avg `-3.5398` n `8`; equity avg `-1.9231` n `127`; fx avg `-0.1138` n `6`; index avg `-0.0987` n `26`; metal avg `-0.3083` n `20`; unknown avg `-0.462` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
