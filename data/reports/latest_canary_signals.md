# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T07:22:21.488673+00:00`
- Correlation status: `ready`
- Asset price records: `529`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.2215` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.3577` n `12`; crypto_alt avg `-0.0264` n `228`; crypto_major avg `0.0471` n `8`; equity avg `0.1691` n `65`; fx avg `0.0033` n `4`; index avg `0.0301` n `23`; metal avg `0.1307` n `18`; unknown avg `1.2245` n `358`
- 1h: commodity avg `-1.1569` n `12`; crypto_alt avg `0.9234` n `228`; crypto_major avg `0.615` n `8`; equity avg `0.4349` n `65`; fx avg `-0.133` n `4`; index avg `0.1233` n `23`; metal avg `0.6651` n `18`; unknown avg `1.2639` n `358`
- 4h: commodity avg `-1.2035` n `12`; crypto_alt avg `1.8596` n `228`; crypto_major avg `1.018` n `8`; equity avg `0.8988` n `65`; fx avg `-0.094` n `4`; index avg `0.2261` n `23`; metal avg `0.8565` n `18`; unknown avg `1.5931` n `356`
- 24h: commodity avg `-2.8244` n `7`; crypto_alt avg `1.3717` n `223`; crypto_major avg `-0.6234` n `7`; equity avg `1.9346` n `47`; fx avg `-0.1666` n `4`; index avg `1.5275` n `6`; metal avg `2.4192` n `7`; unknown avg `1.8601` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1286`, n `525`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `525`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0948`, n `521`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0852`, n `521`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `521`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0801`, n `525`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0789`, n `521`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0736`, n `521`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `521`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0658`, n `525`, weak_sample_signal
