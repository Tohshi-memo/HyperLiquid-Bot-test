# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T13:22:22.411741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `0.1703` n `235`; crypto_major avg `0.0584` n `8`; equity avg `0.0129` n `150`; fx avg `-0.0007` n `6`; index avg `-0.0055` n `26`; metal avg `0.0034` n `20`; unknown avg `0.1568` n `1117`
- 1h: commodity avg `0.0879` n `13`; crypto_alt avg `0.0866` n `235`; crypto_major avg `0.1016` n `8`; equity avg `0.0073` n `150`; fx avg `0.0006` n `6`; index avg `-0.008` n `26`; metal avg `-0.0064` n `20`; unknown avg `0.6648` n `1115`
- 4h: commodity avg `-0.1385` n `13`; crypto_alt avg `0.0325` n `235`; crypto_major avg `-0.1474` n `8`; equity avg `0.0303` n `150`; fx avg `0.0045` n `6`; index avg `-0.0074` n `26`; metal avg `0.004` n `20`; unknown avg `1.3873` n `1109`
- 24h: commodity avg `-0.2367` n `13`; crypto_alt avg `1.8992` n `235`; crypto_major avg `0.1814` n `8`; equity avg `-0.2037` n `150`; fx avg `0.0274` n `6`; index avg `-0.003` n `26`; metal avg `0.0642` n `20`; unknown avg `632.3817` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
