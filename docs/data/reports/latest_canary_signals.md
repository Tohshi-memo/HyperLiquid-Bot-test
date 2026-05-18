# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T03:37:19.683503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1202` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `-0.157` n `228`; crypto_major avg `0.0809` n `8`; equity avg `0.0058` n `66`; fx avg `-0.0033` n `5`; index avg `0.0373` n `23`; metal avg `-0.0497` n `18`; unknown avg `0.043` n `383`
- 1h: commodity avg `-0.0603` n `12`; crypto_alt avg `-0.1832` n `228`; crypto_major avg `-0.2001` n `8`; equity avg `-0.4172` n `66`; fx avg `-0.0008` n `5`; index avg `-0.0317` n `23`; metal avg `-0.2972` n `18`; unknown avg `-0.1535` n `383`
- 4h: commodity avg `0.5676` n `12`; crypto_alt avg `-0.865` n `228`; crypto_major avg `-1.2293` n `8`; equity avg `-0.228` n `66`; fx avg `0.0975` n `5`; index avg `-0.1091` n `23`; metal avg `-1.0482` n `18`; unknown avg `-0.1326` n `383`
- 24h: commodity avg `2.6372` n `12`; crypto_alt avg `-10.9675` n `228`; crypto_major avg `-3.4796` n `8`; equity avg `-3.1349` n `65`; fx avg `-0.0797` n `5`; index avg `-1.7808` n `23`; metal avg `-6.4521` n `18`; unknown avg `550.1381` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
