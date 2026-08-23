# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T17:52:26.338724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0024` n `231`; crypto_major avg `-0.0525` n `8`; equity avg `-0.0033` n `122`; fx avg `0.0014` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.0113` n `793`
- 1h: commodity avg `-0.0187` n `12`; crypto_alt avg `-0.0448` n `231`; crypto_major avg `-0.1675` n `8`; equity avg `0.0189` n `122`; fx avg `0.0043` n `6`; index avg `-0.003` n `25`; metal avg `-0.0224` n `20`; unknown avg `1.0553` n `793`
- 4h: commodity avg `-0.0453` n `12`; crypto_alt avg `0.5213` n `231`; crypto_major avg `-0.4082` n `8`; equity avg `0.1616` n `122`; fx avg `0.0085` n `6`; index avg `0.0315` n `25`; metal avg `0.0146` n `20`; unknown avg `0.5704` n `793`
- 24h: commodity avg `0.0048` n `12`; crypto_alt avg `1.6924` n `231`; crypto_major avg `0.4521` n `8`; equity avg `0.6646` n `122`; fx avg `0.0448` n `6`; index avg `0.0759` n `25`; metal avg `0.0652` n `20`; unknown avg `5.7565` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
