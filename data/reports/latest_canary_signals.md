# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T14:22:30.188146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.1708` n `231`; crypto_major avg `0.2732` n `8`; equity avg `0.0183` n `122`; fx avg `-0.0027` n `6`; index avg `0.0088` n `25`; metal avg `-0.012` n `20`; unknown avg `0.0472` n `793`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `0.7899` n `231`; crypto_major avg `0.3239` n `8`; equity avg `0.0372` n `122`; fx avg `-0.0068` n `6`; index avg `0.0113` n `25`; metal avg `-0.0177` n `20`; unknown avg `0.3904` n `793`
- 4h: commodity avg `-0.0042` n `12`; crypto_alt avg `2.698` n `231`; crypto_major avg `1.3944` n `8`; equity avg `0.2594` n `122`; fx avg `-0.0196` n `6`; index avg `0.0152` n `25`; metal avg `0.0401` n `20`; unknown avg `2.8536` n `793`
- 24h: commodity avg `0.0638` n `12`; crypto_alt avg `2.3935` n `231`; crypto_major avg `1.8847` n `8`; equity avg `0.5445` n `122`; fx avg `0.054` n `6`; index avg `0.0562` n `25`; metal avg `0.0495` n `20`; unknown avg `7.4587` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
