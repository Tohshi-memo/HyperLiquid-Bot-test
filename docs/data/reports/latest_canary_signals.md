# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T00:37:25.300503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `0.1663` n `231`; crypto_major avg `-0.0129` n `8`; equity avg `-0.3198` n `122`; fx avg `0.0067` n `6`; index avg `-0.0561` n `25`; metal avg `-0.0383` n `20`; unknown avg `-0.0141` n `796`
- 1h: commodity avg `-0.014` n `12`; crypto_alt avg `-0.0996` n `231`; crypto_major avg `-0.289` n `8`; equity avg `-0.3905` n `122`; fx avg `0.0254` n `6`; index avg `-0.0944` n `25`; metal avg `-0.0761` n `20`; unknown avg `-0.0615` n `796`
- 4h: commodity avg `0.0711` n `12`; crypto_alt avg `-0.5627` n `231`; crypto_major avg `-0.7787` n `8`; equity avg `-0.4984` n `122`; fx avg `0.0124` n `6`; index avg `-0.1327` n `25`; metal avg `-0.0948` n `20`; unknown avg `-0.3404` n `795`
- 24h: commodity avg `-0.7018` n `12`; crypto_alt avg `-2.4312` n `231`; crypto_major avg `-2.0734` n `8`; equity avg `1.6976` n `122`; fx avg `0.0549` n `6`; index avg `0.1979` n `25`; metal avg `-0.3189` n `20`; unknown avg `-0.4842` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
