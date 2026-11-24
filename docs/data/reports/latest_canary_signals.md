# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T18:37:28.892959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1234` n `13`; crypto_alt avg `0.0936` n `239`; crypto_major avg `0.0023` n `8`; equity avg `0.2095` n `168`; fx avg `0.0091` n `6`; index avg `0.0116` n `27`; metal avg `0.0299` n `20`; unknown avg `1.4955` n `1251`
- 1h: commodity avg `0.1081` n `13`; crypto_alt avg `-0.001` n `239`; crypto_major avg `0.0033` n `8`; equity avg `0.1657` n `168`; fx avg `-0.0032` n `6`; index avg `0.0098` n `27`; metal avg `0.0277` n `20`; unknown avg `0.7641` n `1233`
- 4h: commodity avg `0.2288` n `13`; crypto_alt avg `-0.4991` n `239`; crypto_major avg `-0.4214` n `8`; equity avg `-0.7466` n `168`; fx avg `0.0268` n `6`; index avg `0.0325` n `27`; metal avg `-0.5818` n `20`; unknown avg `-0.2397` n `1227`
- 24h: commodity avg `0.5797` n `13`; crypto_alt avg `-3.6075` n `239`; crypto_major avg `-3.2716` n `8`; equity avg `-3.7782` n `167`; fx avg `0.2742` n `6`; index avg `-0.2264` n `27`; metal avg `-1.1145` n `20`; unknown avg `-0.4678` n `1115`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
