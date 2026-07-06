# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T05:22:25.243274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0392` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.1822` n `229`; crypto_major avg `-0.1136` n `8`; equity avg `-0.0941` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0403` n `20`; unknown avg `-0.2309` n `765`
- 1h: commodity avg `0.0249` n `12`; crypto_alt avg `-0.5415` n `229`; crypto_major avg `-0.3414` n `8`; equity avg `0.1037` n `88`; fx avg `-0.0073` n `6`; index avg `0.0355` n `25`; metal avg `-0.0633` n `20`; unknown avg `-0.1203` n `765`
- 4h: commodity avg `0.0306` n `12`; crypto_alt avg `-1.1665` n `229`; crypto_major avg `-1.1823` n `8`; equity avg `-0.5646` n `88`; fx avg `0.0287` n `6`; index avg `-0.1431` n `25`; metal avg `-0.3774` n `20`; unknown avg `0.5604` n `763`
- 24h: commodity avg `-0.173` n `12`; crypto_alt avg `-0.0216` n `229`; crypto_major avg `1.1937` n `8`; equity avg `-0.6962` n `88`; fx avg `0.0662` n `6`; index avg `-0.0728` n `25`; metal avg `-0.3003` n `20`; unknown avg `1.0401` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
