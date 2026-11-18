# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T20:52:33.391860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `0.108` n `239`; crypto_major avg `0.036` n `8`; equity avg `0.0454` n `164`; fx avg `-0.0075` n `6`; index avg `0.009` n `27`; metal avg `0.0101` n `20`; unknown avg `0.4924` n `1265`
- 1h: commodity avg `-0.0696` n `13`; crypto_alt avg `0.0122` n `239`; crypto_major avg `-0.2238` n `8`; equity avg `0.3006` n `164`; fx avg `0.0074` n `6`; index avg `0.0262` n `27`; metal avg `0.0741` n `20`; unknown avg `174.3032` n `1255`
- 4h: commodity avg `0.2254` n `13`; crypto_alt avg `0.4242` n `239`; crypto_major avg `0.4634` n `8`; equity avg `0.852` n `164`; fx avg `0.0178` n `6`; index avg `0.0916` n `27`; metal avg `0.0654` n `20`; unknown avg `8.6239` n `1255`
- 24h: commodity avg `-0.075` n `13`; crypto_alt avg `-0.3824` n `239`; crypto_major avg `-1.1528` n `8`; equity avg `0.3817` n `164`; fx avg `-0.1676` n `6`; index avg `0.0851` n `27`; metal avg `-1.0363` n `20`; unknown avg `6.4842` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
