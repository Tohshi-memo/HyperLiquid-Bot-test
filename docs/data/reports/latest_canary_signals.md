# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T17:37:35.256990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0372` n `13`; crypto_alt avg `0.0522` n `235`; crypto_major avg `0.0396` n `8`; equity avg `-0.0063` n `150`; fx avg `0.0` n `6`; index avg `-0.0006` n `26`; metal avg `0.0018` n `20`; unknown avg `0.3955` n `1109`
- 1h: commodity avg `-0.0138` n `13`; crypto_alt avg `0.0578` n `235`; crypto_major avg `0.0266` n `8`; equity avg `-0.0347` n `150`; fx avg `-0.0057` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.1381` n `1099`
- 4h: commodity avg `-0.016` n `13`; crypto_alt avg `0.8129` n `235`; crypto_major avg `0.3397` n `8`; equity avg `0.0518` n `150`; fx avg `-0.0055` n `6`; index avg `0.0099` n `26`; metal avg `-0.0166` n `20`; unknown avg `0.4278` n `1085`
- 24h: commodity avg `-0.4498` n `13`; crypto_alt avg `2.5412` n `235`; crypto_major avg `0.8234` n `8`; equity avg `0.2113` n `150`; fx avg `0.0054` n `6`; index avg `0.0406` n `26`; metal avg `0.0097` n `20`; unknown avg `1.566` n `976`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
