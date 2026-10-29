# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T02:07:36.339638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8659` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8124` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1765` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0666` n `13`; crypto_alt avg `-0.7027` n `238`; crypto_major avg `-0.3415` n `8`; equity avg `-0.0909` n `155`; fx avg `0.0475` n `6`; index avg `0.0135` n `27`; metal avg `0.0115` n `20`; unknown avg `0.4622` n `1232`
- 1h: commodity avg `0.003` n `13`; crypto_alt avg `-1.9676` n `238`; crypto_major avg `-1.3765` n `8`; equity avg `-1.1451` n `155`; fx avg `0.018` n `6`; index avg `-0.2` n `27`; metal avg `-0.0302` n `20`; unknown avg `1.8995` n `1230`
- 4h: commodity avg `-0.0492` n `13`; crypto_alt avg `-2.5674` n `238`; crypto_major avg `-1.9671` n `8`; equity avg `-1.1311` n `155`; fx avg `-0.0991` n `6`; index avg `-0.1547` n `27`; metal avg `-0.1012` n `20`; unknown avg `4.4232` n `1148`
- 24h: commodity avg `-0.0932` n `13`; crypto_alt avg `-2.3264` n `238`; crypto_major avg `-1.5784` n `8`; equity avg `-0.9328` n `154`; fx avg `0.0515` n `6`; index avg `-0.139` n `27`; metal avg `-0.0811` n `20`; unknown avg `27.2331` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
