# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T23:22:29.526024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `13`; crypto_alt avg `0.045` n `237`; crypto_major avg `-0.0219` n `8`; equity avg `0.0125` n `152`; fx avg `0.0097` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0009` n `20`; unknown avg `-0.1006` n `1231`
- 1h: commodity avg `-0.0687` n `13`; crypto_alt avg `0.1535` n `237`; crypto_major avg `0.1496` n `8`; equity avg `0.0697` n `152`; fx avg `0.0028` n `6`; index avg `0.01` n `26`; metal avg `0.0125` n `20`; unknown avg `156.0943` n `1231`
- 4h: commodity avg `-0.067` n `13`; crypto_alt avg `0.5203` n `237`; crypto_major avg `0.3299` n `8`; equity avg `0.1123` n `152`; fx avg `0.0129` n `6`; index avg `0.0197` n `26`; metal avg `0.0145` n `20`; unknown avg `-0.0155` n `1137`
- 24h: commodity avg `-0.0675` n `13`; crypto_alt avg `-0.7331` n `237`; crypto_major avg `-0.6685` n `8`; equity avg `0.0531` n `152`; fx avg `-0.0367` n `6`; index avg `0.0094` n `26`; metal avg `-0.0964` n `20`; unknown avg `0.4155` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
