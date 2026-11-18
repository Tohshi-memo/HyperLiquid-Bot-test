# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T17:22:28.852049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1095` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0597` n `13`; crypto_alt avg `0.2574` n `239`; crypto_major avg `0.2817` n `8`; equity avg `0.335` n `164`; fx avg `0.0191` n `6`; index avg `0.0291` n `27`; metal avg `0.0439` n `20`; unknown avg `0.2229` n `1263`
- 1h: commodity avg `-0.2487` n `13`; crypto_alt avg `0.8205` n `239`; crypto_major avg `0.8783` n `8`; equity avg `0.7821` n `164`; fx avg `0.0409` n `6`; index avg `0.1166` n `27`; metal avg `0.0686` n `20`; unknown avg `1.1624` n `1263`
- 4h: commodity avg `-0.48` n `13`; crypto_alt avg `-0.9113` n `239`; crypto_major avg `-1.1634` n `8`; equity avg `-0.9804` n `164`; fx avg `-0.0168` n `6`; index avg `-0.0539` n `27`; metal avg `-0.1638` n `20`; unknown avg `0.5183` n `1257`
- 24h: commodity avg `-0.5212` n `13`; crypto_alt avg `0.1328` n `239`; crypto_major avg `-0.3862` n `8`; equity avg `0.154` n `164`; fx avg `-0.1799` n `6`; index avg `0.032` n `27`; metal avg `-1.2343` n `20`; unknown avg `-0.0682` n `1138`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
