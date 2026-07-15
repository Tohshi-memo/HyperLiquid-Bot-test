# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T18:37:32.687048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.71` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1503` n `12`; crypto_alt avg `-0.0941` n `230`; crypto_major avg `-0.1165` n `8`; equity avg `-0.0451` n `94`; fx avg `-0.0028` n `6`; index avg `-0.0094` n `25`; metal avg `0.0582` n `20`; unknown avg `0.024` n `768`
- 1h: commodity avg `0.1782` n `12`; crypto_alt avg `0.2152` n `230`; crypto_major avg `0.3253` n `8`; equity avg `0.4028` n `94`; fx avg `-0.0013` n `6`; index avg `0.0959` n `25`; metal avg `0.2605` n `20`; unknown avg `-0.0162` n `768`
- 4h: commodity avg `0.1958` n `12`; crypto_alt avg `-0.1508` n `230`; crypto_major avg `-0.279` n `8`; equity avg `0.099` n `94`; fx avg `0.0857` n `6`; index avg `0.0936` n `25`; metal avg `0.1597` n `20`; unknown avg `0.047` n `768`
- 24h: commodity avg `0.116` n `12`; crypto_alt avg `0.7757` n `230`; crypto_major avg `1.2456` n `8`; equity avg `-0.2173` n `93`; fx avg `0.2181` n `6`; index avg `-0.1422` n `25`; metal avg `0.287` n `20`; unknown avg `0.3383` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
