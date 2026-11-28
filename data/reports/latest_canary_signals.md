# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T15:52:25.765647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `0.0506` n `239`; crypto_major avg `0.333` n `8`; equity avg `0.0968` n `168`; fx avg `0.0014` n `6`; index avg `0.0065` n `27`; metal avg `0.0105` n `20`; unknown avg `8.0645` n `1267`
- 1h: commodity avg `-0.0056` n `13`; crypto_alt avg `-0.3754` n `239`; crypto_major avg `0.1141` n `8`; equity avg `0.0087` n `168`; fx avg `0.0009` n `6`; index avg `0.0017` n `27`; metal avg `-0.0234` n `20`; unknown avg `3.8571` n `1259`
- 4h: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.736` n `239`; crypto_major avg `0.1474` n `8`; equity avg `-0.1175` n `168`; fx avg `0.0029` n `6`; index avg `-0.0006` n `27`; metal avg `-0.0384` n `20`; unknown avg `12.0067` n `1245`
- 24h: commodity avg `-0.2229` n `13`; crypto_alt avg `-2.4542` n `239`; crypto_major avg `-1.0653` n `8`; equity avg `0.7103` n `168`; fx avg `-0.0313` n `6`; index avg `0.0689` n `27`; metal avg `0.2613` n `20`; unknown avg `277.7952` n `1094`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
