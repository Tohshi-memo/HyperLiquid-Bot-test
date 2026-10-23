# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T02:52:32.995948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0472` n `13`; crypto_alt avg `-0.0172` n `237`; crypto_major avg `-0.0218` n `8`; equity avg `0.029` n `151`; fx avg `-0.0261` n `6`; index avg `0.0076` n `26`; metal avg `0.0055` n `20`; unknown avg `0.676` n `1233`
- 1h: commodity avg `-0.0475` n `13`; crypto_alt avg `0.6068` n `237`; crypto_major avg `0.383` n `8`; equity avg `0.1526` n `151`; fx avg `0.0247` n `6`; index avg `0.0227` n `26`; metal avg `0.1678` n `20`; unknown avg `0.4672` n `1231`
- 4h: commodity avg `0.0843` n `13`; crypto_alt avg `1.4465` n `237`; crypto_major avg `0.9743` n `8`; equity avg `0.8386` n `151`; fx avg `-0.0107` n `6`; index avg `0.0327` n `26`; metal avg `-0.0141` n `20`; unknown avg `0.8658` n `1225`
- 24h: commodity avg `0.4258` n `13`; crypto_alt avg `-1.8304` n `237`; crypto_major avg `-0.9177` n `8`; equity avg `-3.1271` n `151`; fx avg `-0.1372` n `6`; index avg `-0.4132` n `26`; metal avg `-0.6242` n `20`; unknown avg `52.9037` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
