# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T22:28:23.763141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2266` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0629` n `12`; crypto_alt avg `-0.6911` n `228`; crypto_major avg `-0.6334` n `8`; equity avg `-0.2112` n `77`; fx avg `-0.0273` n `6`; index avg `-0.0986` n `23`; metal avg `-0.1652` n `18`; unknown avg `0.9954` n `687`
- 1h: commodity avg `0.0563` n `12`; crypto_alt avg `-0.7811` n `228`; crypto_major avg `-0.7448` n `8`; equity avg `-0.1295` n `77`; fx avg `-0.0113` n `6`; index avg `-0.1111` n `23`; metal avg `-0.1246` n `18`; unknown avg `0.3553` n `687`
- 4h: commodity avg `0.2355` n `12`; crypto_alt avg `-1.6638` n `228`; crypto_major avg `-1.3809` n `8`; equity avg `-0.2628` n `77`; fx avg `-0.03` n `6`; index avg `-0.1543` n `23`; metal avg `-0.3813` n `18`; unknown avg `0.4821` n `679`
- 24h: commodity avg `0.3336` n `12`; crypto_alt avg `1.3065` n `228`; crypto_major avg `2.8906` n `8`; equity avg `1.5721` n `76`; fx avg `-0.0866` n `6`; index avg `0.7984` n `23`; metal avg `0.0244` n `18`; unknown avg `2.666` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
