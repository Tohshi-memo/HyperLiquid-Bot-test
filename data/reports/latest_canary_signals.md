# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T14:30:53.807292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1605` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0484` n `12`; crypto_alt avg `-0.4166` n `231`; crypto_major avg `-0.4918` n `8`; equity avg `-0.026` n `122`; fx avg `-0.0038` n `6`; index avg `-0.016` n `25`; metal avg `-0.0638` n `20`; unknown avg `-0.0696` n `797`
- 1h: commodity avg `0.1644` n `12`; crypto_alt avg `-0.2606` n `231`; crypto_major avg `-0.4666` n `8`; equity avg `-0.4182` n `122`; fx avg `-0.0153` n `6`; index avg `-0.0748` n `25`; metal avg `-0.0391` n `20`; unknown avg `-0.0868` n `797`
- 4h: commodity avg `0.3949` n `12`; crypto_alt avg `-0.8659` n `231`; crypto_major avg `-1.2016` n `8`; equity avg `-0.4199` n `122`; fx avg `-0.0014` n `6`; index avg `-0.0411` n `25`; metal avg `-0.1375` n `20`; unknown avg `-0.1595` n `797`
- 24h: commodity avg `0.1341` n `12`; crypto_alt avg `-1.95` n `231`; crypto_major avg `-1.9222` n `8`; equity avg `-0.3448` n `122`; fx avg `-0.0572` n `6`; index avg `0.0083` n `25`; metal avg `-0.0326` n `20`; unknown avg `0.4693` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
