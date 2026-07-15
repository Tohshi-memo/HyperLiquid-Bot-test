# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T17:52:33.640921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.1529` n `230`; crypto_major avg `0.1871` n `8`; equity avg `0.2301` n `94`; fx avg `-0.0021` n `6`; index avg `0.0575` n `25`; metal avg `0.0477` n `20`; unknown avg `0.0099` n `768`
- 1h: commodity avg `-0.0647` n `12`; crypto_alt avg `0.3445` n `230`; crypto_major avg `0.3518` n `8`; equity avg `0.8319` n `94`; fx avg `0.0394` n `6`; index avg `0.1754` n `25`; metal avg `0.2814` n `20`; unknown avg `-0.0628` n `768`
- 4h: commodity avg `-0.0621` n `12`; crypto_alt avg `-0.3266` n `230`; crypto_major avg `-0.1674` n `8`; equity avg `-0.8796` n `93`; fx avg `0.1039` n `6`; index avg `-0.0792` n `25`; metal avg `-0.0734` n `20`; unknown avg `-0.03` n `768`
- 24h: commodity avg `0.1328` n `12`; crypto_alt avg `0.4549` n `230`; crypto_major avg `1.1893` n `8`; equity avg `-0.4382` n `93`; fx avg `0.2223` n `6`; index avg `-0.1876` n `25`; metal avg `-0.0324` n `20`; unknown avg `0.3032` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
