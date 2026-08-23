# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T16:22:30.412665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.006` n `231`; crypto_major avg `0.0266` n `8`; equity avg `0.003` n `122`; fx avg `-0.0014` n `6`; index avg `0.0035` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0611` n `793`
- 1h: commodity avg `-0.0414` n `12`; crypto_alt avg `0.1263` n `231`; crypto_major avg `0.0347` n `8`; equity avg `-0.0062` n `122`; fx avg `-0.0059` n `6`; index avg `-0.0152` n `25`; metal avg `0.0259` n `20`; unknown avg `0.2` n `793`
- 4h: commodity avg `-0.0369` n `12`; crypto_alt avg `1.6172` n `231`; crypto_major avg `0.2245` n `8`; equity avg `0.1208` n `122`; fx avg `-0.0108` n `6`; index avg `0.0165` n `25`; metal avg `0.0449` n `20`; unknown avg `1.8784` n `793`
- 24h: commodity avg `0.009` n `12`; crypto_alt avg `1.9393` n `231`; crypto_major avg `1.0587` n `8`; equity avg `0.6138` n `122`; fx avg `0.0229` n `6`; index avg `0.062` n `25`; metal avg `0.0753` n `20`; unknown avg `8.5257` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
