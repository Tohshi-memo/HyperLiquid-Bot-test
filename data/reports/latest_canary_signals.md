# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T14:38:01.645617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1845` n `13`; crypto_alt avg `-0.3139` n `239`; crypto_major avg `-0.6925` n `8`; equity avg `-1.4868` n `163`; fx avg `0.0017` n `6`; index avg `-0.0856` n `27`; metal avg `-0.1088` n `20`; unknown avg `3.5445` n `1266`
- 1h: commodity avg `-0.2859` n `13`; crypto_alt avg `-0.6315` n `239`; crypto_major avg `-0.9151` n `8`; equity avg `-1.8047` n `163`; fx avg `-0.0243` n `6`; index avg `-0.1256` n `27`; metal avg `-0.1046` n `20`; unknown avg `1.5927` n `1264`
- 4h: commodity avg `0.0605` n `13`; crypto_alt avg `-0.6765` n `239`; crypto_major avg `-1.1712` n `8`; equity avg `-2.3956` n `163`; fx avg `-0.0072` n `6`; index avg `-0.2172` n `27`; metal avg `-0.1361` n `20`; unknown avg `0.4497` n `1256`
- 24h: commodity avg `-0.2891` n `13`; crypto_alt avg `-0.7078` n `239`; crypto_major avg `-1.5347` n `8`; equity avg `-1.6023` n `163`; fx avg `-0.1291` n `6`; index avg `-0.0823` n `27`; metal avg `-1.2007` n `20`; unknown avg `2.5909` n `1137`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
