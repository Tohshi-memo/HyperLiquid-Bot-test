# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T00:22:27.560134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1128` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0147` n `231`; crypto_major avg `0.067` n `8`; equity avg `0.1847` n `122`; fx avg `-0.0082` n `6`; index avg `0.0515` n `25`; metal avg `-0.0245` n `20`; unknown avg `0.0305` n `796`
- 1h: commodity avg `-0.029` n `12`; crypto_alt avg `-0.3541` n `231`; crypto_major avg `-0.3566` n `8`; equity avg `-0.1366` n `122`; fx avg `0.008` n `6`; index avg `-0.047` n `25`; metal avg `-0.0478` n `20`; unknown avg `-0.1262` n `795`
- 4h: commodity avg `0.1582` n `12`; crypto_alt avg `-1.0492` n `231`; crypto_major avg `-1.1826` n `8`; equity avg `-0.201` n `122`; fx avg `0.0111` n `6`; index avg `-0.0698` n `25`; metal avg `-0.0834` n `20`; unknown avg `-0.4067` n `795`
- 24h: commodity avg `-0.7348` n `12`; crypto_alt avg `-2.4845` n `231`; crypto_major avg `-1.9344` n `8`; equity avg `2.27` n `122`; fx avg `0.0662` n `6`; index avg `0.304` n `25`; metal avg `-0.1878` n `20`; unknown avg `-0.4114` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
