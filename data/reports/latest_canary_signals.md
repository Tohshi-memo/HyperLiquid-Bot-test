# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T12:37:31.194358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `13`; crypto_alt avg `0.1082` n `238`; crypto_major avg `0.0941` n `8`; equity avg `-0.0384` n `154`; fx avg `0.005` n `6`; index avg `-0.0256` n `27`; metal avg `0.0447` n `20`; unknown avg `0.3761` n `1238`
- 1h: commodity avg `0.0616` n `13`; crypto_alt avg `0.5373` n `238`; crypto_major avg `0.5839` n `8`; equity avg `0.2215` n `154`; fx avg `0.0289` n `6`; index avg `0.0448` n `27`; metal avg `0.0749` n `20`; unknown avg `-0.1506` n `1228`
- 4h: commodity avg `-0.3296` n `13`; crypto_alt avg `0.4633` n `238`; crypto_major avg `0.6674` n `8`; equity avg `1.1675` n `154`; fx avg `0.0164` n `6`; index avg `0.1947` n `27`; metal avg `0.2319` n `20`; unknown avg `14.815` n `1182`
- 24h: commodity avg `-0.1141` n `13`; crypto_alt avg `-0.2456` n `237`; crypto_major avg `0.1823` n `8`; equity avg `0.9963` n `153`; fx avg `-0.0247` n `6`; index avg `0.3687` n `27`; metal avg `-0.2307` n `20`; unknown avg `1020.5873` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
