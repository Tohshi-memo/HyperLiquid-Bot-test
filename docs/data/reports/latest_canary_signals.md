# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T14:52:32.780707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0908` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.5506` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5499` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: crypto_alt avg `-0.5206` n `227`; crypto_major avg `-0.4544` n `7`; metal avg `-0.1224` n `1`; unknown avg `0.0411` n `1041`
- 1h: commodity avg `0.0807` n `13`; crypto_alt avg `-1.0974` n `235`; crypto_major avg `-0.6431` n `8`; equity avg `-0.61` n `151`; fx avg `0.0023` n `6`; index avg `-0.062` n `26`; metal avg `-0.0702` n `20`; unknown avg `-0.273` n `1080`
- 4h: commodity avg `0.3913` n `13`; crypto_alt avg `-2.3276` n `235`; crypto_major avg `-1.6995` n `8`; equity avg `-1.8003` n `151`; fx avg `0.0109` n `6`; index avg `-0.1489` n `26`; metal avg `-0.1496` n `20`; unknown avg `0.0258` n `1057`
- 24h: commodity avg `0.5528` n `13`; crypto_alt avg `-1.4907` n `235`; crypto_major avg `-0.774` n `8`; equity avg `-2.9279` n `151`; fx avg `-0.1111` n `6`; index avg `-0.2986` n `26`; metal avg `-0.1241` n `20`; unknown avg `-0.3432` n `881`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2479`, n `667`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2057`, n `667`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1233`, n `667`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `667`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0945`, n `667`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `667`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0867`, n `667`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
