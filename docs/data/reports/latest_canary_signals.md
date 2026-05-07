# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T06:07:20.142474+00:00`
- Correlation status: `ready`
- Asset price records: `524`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.33` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.161` n `12`; crypto_alt avg `-0.0774` n `228`; crypto_major avg `0.0081` n `8`; equity avg `-0.1133` n `65`; fx avg `0.0191` n `4`; index avg `-0.0189` n `23`; metal avg `0.0547` n `18`; unknown avg `-0.0346` n `356`
- 1h: commodity avg `-0.2283` n `12`; crypto_alt avg `0.18` n `228`; crypto_major avg `0.1685` n `8`; equity avg `0.1594` n `65`; fx avg `0.0019` n `4`; index avg `0.0836` n `23`; metal avg `0.1177` n `18`; unknown avg `-0.1696` n `356`
- 4h: commodity avg `0.0012` n `12`; crypto_alt avg `1.1566` n `228`; crypto_major avg `0.2628` n `8`; equity avg `0.3865` n `65`; fx avg `0.0401` n `4`; index avg `0.14` n `23`; metal avg `-0.1949` n `18`; unknown avg `0.0895` n `356`
- 24h: commodity avg `-1.7571` n `7`; crypto_alt avg `1.1519` n `223`; crypto_major avg `-0.9249` n `7`; equity avg `1.3546` n `47`; fx avg `-0.0206` n `4`; index avg `1.1928` n `6`; metal avg `1.5123` n `7`; unknown avg `1.5328` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `520`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `520`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0844`, n `516`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `516`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `520`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0758`, n `516`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0737`, n `516`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0688`, n `516`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0685`, n `520`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0668`, n `516`, weak_sample_signal
