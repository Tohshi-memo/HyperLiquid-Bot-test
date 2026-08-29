# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T03:37:26.195263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `-0.1928` n `231`; crypto_major avg `-0.0579` n `8`; equity avg `-0.0026` n `127`; fx avg `0.0002` n `6`; index avg `-0.0034` n `26`; metal avg `0.0106` n `20`; unknown avg `0.2714` n `793`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `0.1125` n `231`; crypto_major avg `0.2108` n `8`; equity avg `0.0263` n `127`; fx avg `-0.001` n `6`; index avg `0.0113` n `26`; metal avg `0.0005` n `20`; unknown avg `0.0501` n `793`
- 4h: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.1248` n `231`; crypto_major avg `0.014` n `8`; equity avg `0.1184` n `127`; fx avg `-0.0053` n `6`; index avg `0.0366` n `26`; metal avg `0.0009` n `20`; unknown avg `-0.2565` n `793`
- 24h: commodity avg `-0.1102` n `12`; crypto_alt avg `-1.8026` n `231`; crypto_major avg `-2.5083` n `8`; equity avg `-2.0018` n `127`; fx avg `-0.0874` n `6`; index avg `-0.2028` n `26`; metal avg `-0.2315` n `20`; unknown avg `-0.5255` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
