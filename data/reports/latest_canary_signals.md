# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T13:37:29.554327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `13`; crypto_alt avg `0.0961` n `235`; crypto_major avg `0.0133` n `8`; equity avg `0.007` n `150`; fx avg `-0.007` n `6`; index avg `0.0012` n `26`; metal avg `0.0033` n `20`; unknown avg `0.3791` n `1117`
- 1h: commodity avg `0.0343` n `13`; crypto_alt avg `0.2092` n `235`; crypto_major avg `0.114` n `8`; equity avg `0.0172` n `150`; fx avg `-0.0079` n `6`; index avg `-0.0057` n `26`; metal avg `0.0037` n `20`; unknown avg `0.8231` n `1115`
- 4h: commodity avg `0.0148` n `13`; crypto_alt avg `0.0584` n `235`; crypto_major avg `-0.1169` n `8`; equity avg `0.0388` n `150`; fx avg `-0.0014` n `6`; index avg `-0.0095` n `26`; metal avg `0.0074` n `20`; unknown avg `1.5197` n `1109`
- 24h: commodity avg `-0.2889` n `13`; crypto_alt avg `2.3701` n `235`; crypto_major avg `0.6851` n `8`; equity avg `0.2305` n `150`; fx avg `0.0179` n `6`; index avg `0.0328` n `26`; metal avg `-0.0134` n `20`; unknown avg `631.1005` n `956`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
