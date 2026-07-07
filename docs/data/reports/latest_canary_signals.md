# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T20:52:28.226787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2904` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `-0.1655` n `229`; crypto_major avg `-0.1404` n `8`; equity avg `0.0187` n `91`; fx avg `-0.0015` n `6`; index avg `-0.0011` n `25`; metal avg `0.0171` n `20`; unknown avg `0.0139` n `763`
- 1h: commodity avg `0.1037` n `12`; crypto_alt avg `-0.3035` n `229`; crypto_major avg `-0.3508` n `8`; equity avg `0.2237` n `91`; fx avg `0.0099` n `6`; index avg `0.0348` n `25`; metal avg `-0.0632` n `20`; unknown avg `0.0504` n `763`
- 4h: commodity avg `0.4137` n `12`; crypto_alt avg `-1.6842` n `229`; crypto_major avg `-1.3706` n `8`; equity avg `-0.6167` n `91`; fx avg `-0.0047` n `6`; index avg `-0.0802` n `25`; metal avg `-0.4333` n `20`; unknown avg `0.4843` n `761`
- 24h: commodity avg `0.9205` n `12`; crypto_alt avg `-2.1194` n `229`; crypto_major avg `-1.2629` n `8`; equity avg `-3.1765` n `91`; fx avg `-0.2431` n `6`; index avg `-0.5837` n `25`; metal avg `-0.5865` n `20`; unknown avg `-0.196` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
