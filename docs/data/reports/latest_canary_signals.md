# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T17:12:53.587338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1018` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0552` n `12`; crypto_alt avg `-0.2102` n `230`; crypto_major avg `-0.4418` n `8`; equity avg `-0.122` n `112`; fx avg `-0.0019` n `6`; index avg `-0.005` n `25`; metal avg `0.0165` n `20`; unknown avg `0.2026` n `782`
- 1h: commodity avg `-0.0326` n `12`; crypto_alt avg `-0.4005` n `230`; crypto_major avg `-0.7791` n `8`; equity avg `-0.5328` n `112`; fx avg `-0.0087` n `6`; index avg `-0.0355` n `25`; metal avg `-0.0951` n `20`; unknown avg `0.4099` n `782`
- 4h: commodity avg `0.3081` n `12`; crypto_alt avg `-0.539` n `230`; crypto_major avg `-1.23` n `8`; equity avg `-0.7591` n `112`; fx avg `0.0006` n `6`; index avg `-0.1282` n `25`; metal avg `-0.1829` n `20`; unknown avg `0.3398` n `782`
- 24h: commodity avg `0.338` n `12`; crypto_alt avg `-0.5601` n `230`; crypto_major avg `-0.7418` n `8`; equity avg `0.5624` n `112`; fx avg `-0.1434` n `6`; index avg `-0.0343` n `25`; metal avg `0.2452` n `20`; unknown avg `-0.09` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
