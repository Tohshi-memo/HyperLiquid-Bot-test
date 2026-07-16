# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T23:43:35.231217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0016` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.1685` n `230`; crypto_major avg `0.1051` n `8`; equity avg `-0.0976` n `94`; fx avg `0.0054` n `6`; index avg `-0.0208` n `25`; metal avg `0.0045` n `20`; unknown avg `0.0976` n `768`
- 1h: commodity avg `-0.0243` n `12`; crypto_alt avg `-0.4996` n `230`; crypto_major avg `-0.544` n `8`; equity avg `-0.5278` n `94`; fx avg `0.0209` n `6`; index avg `-0.0376` n `25`; metal avg `0.0233` n `20`; unknown avg `-0.221` n `768`
- 4h: commodity avg `0.113` n `12`; crypto_alt avg `-0.8811` n `230`; crypto_major avg `-1.0001` n `8`; equity avg `-0.6961` n `94`; fx avg `0.0041` n `6`; index avg `0.0015` n `25`; metal avg `0.0161` n `20`; unknown avg `-0.3754` n `768`
- 24h: commodity avg `-0.1542` n `12`; crypto_alt avg `-1.9111` n `230`; crypto_major avg `-2.9023` n `8`; equity avg `-4.3967` n `94`; fx avg `-0.1351` n `6`; index avg `-0.589` n `25`; metal avg `-0.8398` n `20`; unknown avg `-0.5773` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
