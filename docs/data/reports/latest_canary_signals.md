# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T13:52:34.584396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3064` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0994` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0795` n `12`; crypto_alt avg `-0.1778` n `228`; crypto_major avg `-0.3926` n `8`; equity avg `-0.2977` n `86`; fx avg `-0.0033` n `6`; index avg `-0.021` n `23`; metal avg `0.3075` n `20`; unknown avg `-0.1872` n `764`
- 1h: commodity avg `-0.1964` n `12`; crypto_alt avg `-1.2439` n `228`; crypto_major avg `-1.1155` n `8`; equity avg `-0.8811` n `86`; fx avg `0.0067` n `6`; index avg `-0.0161` n `23`; metal avg `0.1471` n `20`; unknown avg `0.1675` n `764`
- 4h: commodity avg `-0.35` n `12`; crypto_alt avg `-1.3664` n `228`; crypto_major avg `-1.3211` n `8`; equity avg `-1.1183` n `86`; fx avg `-0.0654` n `6`; index avg `-0.0147` n `23`; metal avg `-0.8169` n `20`; unknown avg `0.2133` n `764`
- 24h: commodity avg `-0.6769` n `12`; crypto_alt avg `-1.956` n `228`; crypto_major avg `-1.4865` n `8`; equity avg `2.5218` n `86`; fx avg `-0.0101` n `6`; index avg `0.0572` n `23`; metal avg `-1.4258` n `20`; unknown avg `-0.44` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
