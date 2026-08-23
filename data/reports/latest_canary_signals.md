# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T20:22:32.617263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `0.2419` n `231`; crypto_major avg `0.2776` n `8`; equity avg `0.0061` n `122`; fx avg `-0.02` n `6`; index avg `-0.0042` n `25`; metal avg `0.0158` n `20`; unknown avg `-0.0083` n `793`
- 1h: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.0095` n `231`; crypto_major avg `0.1416` n `8`; equity avg `-0.0149` n `122`; fx avg `-0.0564` n `6`; index avg `-0.0049` n `25`; metal avg `0.0138` n `20`; unknown avg `0.4746` n `793`
- 4h: commodity avg `-0.0431` n `12`; crypto_alt avg `0.571` n `231`; crypto_major avg `0.4335` n `8`; equity avg `0.2714` n `122`; fx avg `-0.0559` n `6`; index avg `0.0525` n `25`; metal avg `0.0203` n `20`; unknown avg `0.8683` n `793`
- 24h: commodity avg `-0.1027` n `12`; crypto_alt avg `2.3391` n `231`; crypto_major avg `0.1891` n `8`; equity avg `0.7388` n `122`; fx avg `-0.0519` n `6`; index avg `0.1263` n `25`; metal avg `0.0953` n `20`; unknown avg `5.5838` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
