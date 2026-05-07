# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T08:37:22.419326+00:00`
- Correlation status: `ready`
- Asset price records: `534`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2003` n `12`; crypto_alt avg `0.0151` n `228`; crypto_major avg `-0.0143` n `8`; equity avg `-0.0245` n `65`; fx avg `-0.0298` n `4`; index avg `-0.0183` n `23`; metal avg `-0.0224` n `18`; unknown avg `0.1872` n `358`
- 1h: commodity avg `0.2199` n `12`; crypto_alt avg `-0.0863` n `228`; crypto_major avg `-0.2749` n `8`; equity avg `-0.2565` n `65`; fx avg `0.0201` n `4`; index avg `-0.0053` n `23`; metal avg `0.0773` n `18`; unknown avg `0.213` n `358`
- 4h: commodity avg `-0.8306` n `12`; crypto_alt avg `1.3596` n `228`; crypto_major avg `0.778` n `8`; equity avg `0.4537` n `65`; fx avg `-0.0246` n `4`; index avg `0.2489` n `23`; metal avg `1.2504` n `18`; unknown avg `0.6402` n `356`
- 24h: commodity avg `-2.0794` n `7`; crypto_alt avg `0.8008` n `223`; crypto_major avg `-0.9758` n `7`; equity avg `1.3497` n `47`; fx avg `0.0026` n `4`; index avg `1.2623` n `6`; metal avg `2.1561` n `7`; unknown avg `1.1248` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1328`, n `530`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1253`, n `530`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.104`, n `530`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0927`, n `526`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0837`, n `526`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0819`, n `526`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `526`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0766`, n `526`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `526`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0663`, n `530`, weak_sample_signal
