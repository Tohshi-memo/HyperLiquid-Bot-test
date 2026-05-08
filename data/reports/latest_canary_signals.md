# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T06:00:20.818520+00:00`
- Correlation status: `ready`
- Asset price records: `523`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.34` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0088` n `12`; crypto_alt avg `-0.0835` n `228`; crypto_major avg `-0.079` n `8`; equity avg `0.0899` n `65`; fx avg `0.0122` n `4`; index avg `0.0436` n `23`; metal avg `0.0057` n `18`; unknown avg `-0.247` n `358`
- 1h: commodity avg `-0.0178` n `12`; crypto_alt avg `0.5555` n `228`; crypto_major avg `0.2422` n `8`; equity avg `0.3433` n `65`; fx avg `-0.0141` n `4`; index avg `0.1161` n `23`; metal avg `0.1765` n `18`; unknown avg `-0.0505` n `358`
- 4h: commodity avg `0.0237` n `12`; crypto_alt avg `1.0472` n `228`; crypto_major avg `0.0813` n `8`; equity avg `0.5226` n `65`; fx avg `0.0416` n `4`; index avg `0.1456` n `23`; metal avg `-0.3366` n `18`; unknown avg `-0.1019` n `358`
- 24h: commodity avg `-1.9066` n `7`; crypto_alt avg `1.4518` n `223`; crypto_major avg `-0.681` n `7`; equity avg `1.5841` n `47`; fx avg `-0.0628` n `4`; index avg `1.2068` n `6`; metal avg `1.6023` n `7`; unknown avg `1.8449` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `519`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `519`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0826`, n `515`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `519`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `515`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `515`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0723`, n `515`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `519`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0675`, n `515`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0666`, n `515`, weak_sample_signal
