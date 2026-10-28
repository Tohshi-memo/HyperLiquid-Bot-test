# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T04:22:30.686076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.61` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0032` n `13`; crypto_alt avg `-0.1854` n `238`; crypto_major avg `-0.0836` n `8`; equity avg `-0.0564` n `154`; fx avg `-0.0097` n `6`; index avg `-0.0118` n `27`; metal avg `-0.0076` n `20`; unknown avg `1.8744` n `1236`
- 1h: commodity avg `0.0232` n `13`; crypto_alt avg `-0.2553` n `238`; crypto_major avg `-0.1389` n `8`; equity avg `0.0234` n `154`; fx avg `0.0028` n `6`; index avg `-0.0186` n `27`; metal avg `-0.0555` n `20`; unknown avg `0.8929` n `1222`
- 4h: commodity avg `0.1137` n `13`; crypto_alt avg `0.132` n `238`; crypto_major avg `0.2509` n `8`; equity avg `0.8337` n `154`; fx avg `0.113` n `6`; index avg `0.0946` n `27`; metal avg `-0.1806` n `20`; unknown avg `0.0146` n `1214`
- 24h: commodity avg `0.0376` n `13`; crypto_alt avg `2.0098` n `237`; crypto_major avg `1.8965` n `8`; equity avg `3.2095` n `154`; fx avg `0.0951` n `6`; index avg `0.5149` n `27`; metal avg `0.087` n `20`; unknown avg `6.7894` n `1014`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
