# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T02:52:28.272782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8578` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.85` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0294` n `13`; crypto_alt avg `0.1976` n `238`; crypto_major avg `0.3113` n `8`; equity avg `0.2749` n `155`; fx avg `-0.0039` n `6`; index avg `0.0692` n `27`; metal avg `0.0765` n `20`; unknown avg `6.2088` n `1236`
- 1h: commodity avg `-0.0734` n `13`; crypto_alt avg `-0.958` n `238`; crypto_major avg `-0.3712` n `8`; equity avg `-0.1157` n `155`; fx avg `0.0306` n `6`; index avg `0.0342` n `27`; metal avg `-0.0644` n `20`; unknown avg `2.032` n `1226`
- 4h: commodity avg `-0.033` n `13`; crypto_alt avg `-2.7101` n `238`; crypto_major avg `-1.9609` n `8`; equity avg `-0.9477` n `155`; fx avg `-0.1081` n `6`; index avg `-0.1031` n `27`; metal avg `-0.1109` n `20`; unknown avg `4.8055` n `1166`
- 24h: commodity avg `-0.0146` n `13`; crypto_alt avg `-2.6165` n `238`; crypto_major avg `-1.718` n `8`; equity avg `-1.1541` n `154`; fx avg `0.0031` n `6`; index avg `-0.1413` n `27`; metal avg `-0.169` n `20`; unknown avg `25.9801` n `990`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
