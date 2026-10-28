# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T15:22:28.574582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1189` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0822` n `13`; crypto_alt avg `0.1596` n `238`; crypto_major avg `0.0956` n `8`; equity avg `0.1242` n `155`; fx avg `-0.0055` n `6`; index avg `0.0184` n `27`; metal avg `0.0027` n `20`; unknown avg `0.1327` n `1238`
- 1h: commodity avg `-0.089` n `13`; crypto_alt avg `0.6766` n `238`; crypto_major avg `0.3604` n `8`; equity avg `0.2417` n `155`; fx avg `0.0345` n `6`; index avg `0.0379` n `27`; metal avg `0.0288` n `20`; unknown avg `-0.0492` n `1230`
- 4h: commodity avg `0.0625` n `13`; crypto_alt avg `-0.8364` n `238`; crypto_major avg `-1.0634` n `8`; equity avg `-0.4286` n `155`; fx avg `0.1034` n `6`; index avg `0.0555` n `27`; metal avg `0.0062` n `20`; unknown avg `1.0823` n `1152`
- 24h: commodity avg `0.4969` n `13`; crypto_alt avg `0.2432` n `238`; crypto_major avg `0.1986` n `8`; equity avg `1.5237` n `154`; fx avg `0.2097` n `6`; index avg `0.2973` n `27`; metal avg `-0.1507` n `20`; unknown avg `7.0811` n `1100`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
