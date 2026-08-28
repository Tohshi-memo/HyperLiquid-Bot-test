# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T23:52:26.567641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.22` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `0.0226` n `231`; crypto_major avg `0.025` n `8`; equity avg `0.0104` n `127`; fx avg `-0.0137` n `6`; index avg `0.0018` n `26`; metal avg `-0.0107` n `20`; unknown avg `-0.0776` n `793`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `0.2318` n `231`; crypto_major avg `0.0197` n `8`; equity avg `0.0071` n `127`; fx avg `-0.0109` n `6`; index avg `0.0006` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.1238` n `793`
- 4h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.713` n `231`; crypto_major avg `0.4767` n `8`; equity avg `0.0153` n `127`; fx avg `-0.0311` n `6`; index avg `-0.0115` n `26`; metal avg `0.0604` n `20`; unknown avg `0.2647` n `793`
- 24h: commodity avg `-0.1233` n `12`; crypto_alt avg `-2.9289` n `231`; crypto_major avg `-3.514` n `8`; equity avg `-1.9197` n `127`; fx avg `-0.1459` n `6`; index avg `-0.1517` n `26`; metal avg `-0.3049` n `20`; unknown avg `-0.5819` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
