# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T17:07:35.121422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.3748` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1049` n `13`; crypto_alt avg `0.5046` n `239`; crypto_major avg `0.7067` n `8`; equity avg `0.7001` n `164`; fx avg `0.0059` n `6`; index avg `0.0876` n `27`; metal avg `0.0425` n `20`; unknown avg `1.4202` n `1259`
- 1h: commodity avg `-0.1635` n `13`; crypto_alt avg `-0.0616` n `239`; crypto_major avg `-0.0349` n `8`; equity avg `-0.1066` n `164`; fx avg `0.0014` n `6`; index avg `0.021` n `27`; metal avg `-0.0277` n `20`; unknown avg `1.7441` n `1261`
- 4h: commodity avg `-0.5255` n `13`; crypto_alt avg `-0.9712` n `239`; crypto_major avg `-1.4478` n `8`; equity avg `-1.2242` n `164`; fx avg `-0.0439` n `6`; index avg `-0.073` n `27`; metal avg `-0.1789` n `20`; unknown avg `2.8902` n `1257`
- 24h: commodity avg `-0.4661` n `13`; crypto_alt avg `0.0029` n `239`; crypto_major avg `-0.5427` n `8`; equity avg `0.13` n `164`; fx avg `-0.1937` n `6`; index avg `0.0523` n `27`; metal avg `-1.227` n `20`; unknown avg `0.1759` n `1138`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
