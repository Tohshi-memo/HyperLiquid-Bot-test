# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T14:07:36.884111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2891` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0808` n `13`; crypto_alt avg `0.244` n `238`; crypto_major avg `0.299` n `8`; equity avg `0.2037` n `155`; fx avg `0.0031` n `6`; index avg `0.0518` n `27`; metal avg `-0.0269` n `20`; unknown avg `3.3757` n `1212`
- 1h: commodity avg `0.0408` n `13`; crypto_alt avg `-0.2257` n `238`; crypto_major avg `-0.1747` n `8`; equity avg `-0.4171` n `155`; fx avg `0.039` n `6`; index avg `-0.0062` n `27`; metal avg `-0.1169` n `20`; unknown avg `3.8456` n `1198`
- 4h: commodity avg `0.1435` n `13`; crypto_alt avg `-1.2077` n `238`; crypto_major avg `-1.2199` n `8`; equity avg `-0.4571` n `155`; fx avg `0.0805` n `6`; index avg `0.0692` n `27`; metal avg `0.0164` n `20`; unknown avg `5.1284` n `1194`
- 24h: commodity avg `0.2442` n `13`; crypto_alt avg `0.8116` n `238`; crypto_major avg `0.823` n `8`; equity avg `1.8917` n `154`; fx avg `0.1444` n `6`; index avg `0.4285` n `27`; metal avg `0.0423` n `20`; unknown avg `4.8916` n `1046`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
