# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T12:22:32.504077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1814` n `12`; crypto_alt avg `0.0821` n `229`; crypto_major avg `0.1274` n `8`; equity avg `0.1421` n `91`; fx avg `-0.007` n `6`; index avg `0.0511` n `25`; metal avg `0.0247` n `20`; unknown avg `-0.0325` n `766`
- 1h: commodity avg `-0.1155` n `12`; crypto_alt avg `-0.0556` n `229`; crypto_major avg `-0.1106` n `8`; equity avg `-0.268` n `91`; fx avg `-0.0003` n `6`; index avg `-0.032` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.0667` n `766`
- 4h: commodity avg `0.0737` n `12`; crypto_alt avg `0.1453` n `229`; crypto_major avg `0.0876` n `8`; equity avg `0.5969` n `91`; fx avg `0.0035` n `6`; index avg `0.0725` n `25`; metal avg `-0.0437` n `20`; unknown avg `-0.0613` n `765`
- 24h: commodity avg `-1.0766` n `12`; crypto_alt avg `1.1907` n `229`; crypto_major avg `1.8452` n `8`; equity avg `0.4449` n `91`; fx avg `-0.1128` n `6`; index avg `0.1607` n `25`; metal avg `0.0038` n `20`; unknown avg `0.0955` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
